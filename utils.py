"""Helper commands for fluent_TUI"""

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