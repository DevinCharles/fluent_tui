"""Helper commands for fluent_TUI"""

def multigzip(folder=None, compression_level=9, rezip=False):
## TODO: tqdm_notebook?
## TODO: Maybe split this into a single file GZIP application and one that
##       operates on a folder, or one that'll walk
## TODO: This opens N process of 7z (one for each file). May handle
##       this by multiprossing number of cores, splitting the list
    try: from tqdm import tqdm as tqdm
    except: tqdm = lambda x: x
    from subprocess import Popen, PIPE
    import os
    if folder is None:
        folder = gui_open(directory=True)
    if folder is None:
        return
    results = []
    for file in tqdm(os.listdir(folder)):
        if (file[-4::] in ['.dat','.cas']) or (rezip and (file[-3::] =='.gz')):
            pipe = Popen(['7z', 'a', '-sdel', '-mx'+str(compression_level),
                os.path.join(folder,file+'.gz'),
                os.path.join(folder,file)])
    #            stdout=PIPE, stderr=PIPE);
    #        out, err = pipe.communicate()
    #        results.append(out.decode())
    
    #for result,file in zip(results,os.listdir(folder)):
    #    if 'Everything is Ok' in result:
    #        print(file+' - OKAY')
    #    else:
    #        print(file+' - Failed!')
    #        print(result)
    #return results
    
def gui_open(plot=None,directory=False,title=''):
    import tkinter as tk
    from tkinter import filedialog,messagebox
    root = tk.Tk()
    root.withdraw()
    if directory:
        folder = filedialog.askdirectory(title=title)
        return folder
    fname = filedialog.askopenfilename(title=title)
    if plot is None:
        plot = messagebox.askyesno("","Plot Results?")
    return fname,plot

def regrid(x,y,z,dx,dy):
    """Restructure flattened arrays to NxM arrays
    dx,dy are the smallest step you expect to see in x,y"""
    import numpy as np
    idx = [val>0.9*dx for val in np.diff([x.min()-dx]+np.unique(x).tolist())]
    xs = np.unique(x)[idx]
    xi = [np.argmin(abs(xs-val)) for val in x]

    idx = [val>0.9*dy for val in np.diff([y.min()-dy]+np.unique(y).tolist())]
    ys = np.unique(y)[idx]
    yi = [np.argmin(abs(ys-val)) for val in y]

    X = np.nan*np.ones((len(ys),len(xs)))
    Y = np.copy(X)
    Z = np.copy(X)

    for xval,yval,zval,i,j in zip(x,y,z,yi,xi):
        X[i,j] = xval
        Y[i,j] = yval
        Z[i,j] = zval
    return X,Y,Z
    
def integrate(x,y,z=None):
    """Simple Line and Surface Integration
    """
    from scipy.integrate import trapz, simps
    if z is None:
        return trapz(y,x)
    else:
        return simps(simps(z,x[0,:]),y[:,0])

def fluent_connect(verbose=False):
    '''Tool for connecting to the fluent and cx process - WIP'''
    import psutil
    ##TODO: handle ModuleNotFoundError for psutil with gui open dir
    try:
        flu_pid = [p.info for p in psutil.process_iter(attrs=['pid', 'name']) if 'fluent' in p.info['name']][0]['pid']
    except IndexError:
        print('Could not connect to Fluent')
        raise
        
    flu_dict = psutil.Process(flu_pid).as_dict()
    flu_version = flu_dict['environ']['FLUENT_PROD_DIR'].split('\\')[-1].split('fluent')[1].replace('.','')
    flu_cwd = flu_dict['cwd']

    cx_pid = [p.info for p in psutil.process_iter(attrs=['pid', 'name']) if 'cx'+flu_version in p.info['name']][0]['pid']
    cx_dict = psutil.Process(cx_pid).as_dict()
    
    if verbose:
        print('Connected to Fluent')
        print('-------------------')
        fmt = lambda x,y: '{0:.<20}{1:.>100}'.format(x.replace('_',' ').title()+':',y)
        cwd = flu_cwd
        if len(cwd) > 100:
            cwd = cwd[0:47]+'...'+cwd[-50::]
        cmdline = ' '.join(flu_dict['cmdline'])
        host,user = flu_dict['username'].split('\\')
        processors = ','.join([str(x) for x in flu_dict['cpu_affinity']])
        d = dict(host=host,version=flu_version,username=user,
        processors=processors,start_command=cmdline,working_directory=cwd)
        [print(fmt(k,v)) for k,v in d.items()];
    
    return flu_cwd
        
def parse_residuals(fname):
    '''Tool to parse residual data from Transcript File'''
    import pandas as pd
    import numpy as np
    import re
    if fname is None:
        fname,plot = gui_open(plot)
    str_data = []
    re_str = '^\s{0,5}(?P<iter>\d{1,6})' \
    '(?P<floats>(?:\s{1,3}\d{1,2}\.\d{4}e[+-]\d{2})+)'\
    '\s{1,3}(?P<time>\d{1,2}:\d{2}:\d{2})'\
    '\s{1,4}(?P<left>\d{1,4})$'
    regexp = re.compile(re_str,re.M)
    # Read line by line (might be a large file?)
    # Previously: regexp.findall(string)
    with open(fname,'r') as file:
        for line in file:
            if regexp.match(line):
                str_data.append(regexp.match(line).groups())
    # Open beginning to find names
    all_names = []
    with open(fname,'r') as file:
        for line in file:
            if ('iter' in line) & ('continuity' in line):
                all_names.append(line)
    
    # If we haven't started running yet...
    if len(all_names) < 1:
        print('It appears no iterations have been performed yet.')
        return
    if 'iter' not in all_names[-1]:
        print('It appears no iterations have been performed yet.')
        return
    
    names = [re.sub('\s+',' ',re.search('^\s+iter.*$',name,
        re.M).group().replace('/iter',' iter-left')).strip().split(' ') for
        name in all_names]
    # Checking for a change in the number of column names (we've changed the
    # residuals we're tracking somewhere')
    if np.any(np.diff([len(n) for n in names])<0):
        ind = np.where(np.diff([len(n) for n in names])<0)[0][-1]+1
        names = names[ind]
    else:
        names = names[0]
    names[0] = 'iteration'
    dtypes={key:float for key in names[1:-2]}
    dtypes.update({names[0]:int,names[-1]:int,names[-2]:'O'})
    data = [[row[0],*re.sub('\s+',' ',row[1]).strip().split(' '),*row[2::]] for row in str_data]
    # Checking for a change in the number of column names (we've changed the
    # residuals we're tracking somewhere')
    if np.any(np.diff([len(d) for d in data])<0):
        ind = np.where(np.diff([len(d) for d in data])<0)[0][-1]+1
        data = data[ind::]
    df = pd.DataFrame(data,columns=names).astype(dtype=dtypes)
    df['time'] = pd.to_timedelta(df['time'])
    df['converged']=df['iter-left'].diff()>0
    df['relative-total-time'] = df.time[df['converged']].cumsum()
    df['relative-total-time'] = df['relative-total-time'].fillna(method='backfill')
    df['relative-time-step'] = df['converged'].cumsum()
    df.index = df.iteration
    return df

def parse_outfile(fname=None,plot=None):
    """Simple tool to parse report output files to dataframe"""
    import pandas as pd
    if fname is None:
        fname,plot = gui_open(plot)
    with open(fname, 'r') as file:
        data = file.read().split('\n')
        headers = [x.replace(' ','-').lower() for x in data[2].strip('(")').split('" "')]
    df = pd.read_csv(fname,delimiter=' ', skiprows=3, names=headers)
    if plot:
        if 'flow-time' in df.columns:
            x = 'flow-time'
        elif 'time-step' in df.columns:
            x = 'time-step'
        elif 'iteration' in df.columns:
            x = 'iteration'
        else:
            x = None
        print(x)
        dfp = df.copy().drop(x,1)
        dfp.index = df[x]
        dfp.plot(subplots=True)
    return df
    
def parse_xy(fname=None,plot=None):
    import re
    import pandas as pd
    if fname is None:
        fname,plot = gui_open(plot)
    with open(fname,'rt') as txtfile:
        txt = txtfile.read()

    title = re.search('\(title\s"(.*)"\)?',txt).groups()[0]
    columns = re.search('\(labels\s"(.*)"\s"(.*)"\)?',txt).groups()
    raw = txt[re.search('\n\n\(\(.*\)\n',txt).span()[1]::].split('\n')[0:-2]
    df = pd.DataFrame(
        [row.split('\t') for row in raw],
        columns=columns,
    ).astype(float)
    if plot:
        ax = df.plot.scatter(x=columns[0],y=columns[1])
        ax.grid(True,'both','both')
        return df, ax
    else:
        return df
        
def parse_prof_csv(fname=None,plot=None):
    import pandas as pd
    if fname is None:
        fname,plot = gui_open(plot)
    with open(fname,'rt') as txtfile:
        txt = txtfile.read()
        header = len(txt.lower().split('[data]')[0].split('\n'))
    df = pd.read_csv(
        fname,
        header=header,
        skip_blank_lines=False,
    ).astype(float)
    if plot:
        columns = df.columns
        axes = []
        axes.append(df.plot.scatter(x=columns[0],y=columns[-1]))
        axes.append(df.plot.scatter(x=columns[1],y=columns[-1]))
        axes.append(df.plot.scatter(x=columns[2],y=columns[-1]))
        [ax.grid(True,'both','both') for ax in axes]
        return df, axes
    else:
        return df

def copy_to_clipboard(command):
    from tkinter import Tk
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(command)
    r.update() # now it stays on the clipboard after the window is closed
    r.destroy()

def journal_writer(commands, filename=None, append=True, version='19.1'):
    """Writes tui commands to a journal file"""
    from os import path
    from datetime import datetime
    
    if commands == []:
        print('Nothing to write!')
        return
    
    if filename is None:
        filename = path.join(path.expanduser('~'),'Desktop','journal.jou')
        
    if path.exists(filename) and append:
        write = 'a'
    else:
        write = 'w'
        
    with open(filename,write) as file:
        if write == 'w':
            file.write('; This document was created by fluentTUI\n\n')
            #file.write('/file/set-tui-version "'+str(version)+'"\n')
        file.write(''.join(commands))
        file.write('\n; Last Updated on ' + datetime.strftime(datetime.now(),'%c') +' by fluentTUI\n')
        
    outcommand = '/file/read-journal/ "'+filename+'"'
    copy_to_clipboard(outcommand)
    print(outcommand)