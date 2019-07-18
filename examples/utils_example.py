import fluent_tui as tui
from fluent_tui.utils import regrid, integrate
from matplotlib import pyplot as plt
import numpy as np
%matplotlib qt5

def figure(style='2d'):
    if '3' in style:
        from mpl_toolkits.mplot3d import Axes3D
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
    else:
        fig,ax = plt. subplots()
    return fig,ax

def offset(x,xdir='max',val=0.1):
    if xdir == 'max':
        return x.max()+val*(x.max()-x.min())
    else:
        return x.min()-val*(x.max()-x.min())
    
## Get Some Profile Data
df = tui.utils.parse_prof_csv(plot=False)
#print(df.head())

## Attempt to reshape the flattend data back into a grid...
# These are the smallest mesh step size expected
dx = 5.0e-3
dy = 0.5e-3

x,y,z = ['z','y','mean-velocity-magnitude']

X,Y,Z = regrid(df[x],df[y],df[z],dx,dy)

## Plot it, to see if all went well
fig,ax = figure('3D')
ax.plot_surface(X,Y,Z,cmap='inferno',edgecolor='k')
ax.set_xlabel(x)
ax.set_ylabel(y)
ax.set_title(z.replace('-',' ').title())
ax.set_aspect(1)

fig,ax = figure('3D')
ax.contourf(X,Y,Z,zdir='x',offset=offset(X,'min'),levels=20,cmap='inferno')
ax.contourf(X,Y,Z,zdir='y',offset=offset(Y,'max'),levels=20,cmap='inferno')
ax.contourf(X,Y,Z,zdir='z',offset=offset(Z,'min'),levels=20,cmap='inferno')
ax.set_xlabel(x)
ax.set_ylabel(y)
ax.set_title(z.replace('-',' ').title())
ax.set_aspect(1)

fig,ax = figure('2D')
ax.contourf(X,Y,Z,zdir='x',offset=offset(X,'min'),levels=20,cmap='inferno')
ax.set_xlabel(x)
ax.set_ylabel(y)
ax.set_title(z.replace('-',' ').title())
ax.set_aspect(1)

## Try out some integration...
fig,ax = figure('2D')
idx = ((0<X) & (X<=0.0025))
ax.plot(Z[idx],Y[idx])
ax.set_xlabel(z)
ax.set_ylabel(y)
ax.set_title(z.replace('-',' ').title()+'\n on line z=0.0025\n at x=0 plane')
ax.grid(True,'both','both')
Q = integrate(Y[idx],Z[idx])
Um = Q/(Y[idx].max()-Y[idx].min())
#txt = '$Q = \int_0^h U \ \mathrm{d}y \ \mathrm{d}z$\nFlow Rate: '+
#    '{:1.3f}$[m^3 s^-1]$'.format(Q)
txt = '$U_m ={:1.3f}$'.format(Um)+' $[m \ s^{-1}]$'
ax.text(np.mean(ax.get_xlim()),np.mean(ax.get_ylim()),txt,ha='center',va='center')

fig,ax = figure('3D')
ax.plot_surface(X,Y,Z,cmap='inferno',edgecolor='k')
ax.set_zlabel(z)
ax.set_xlabel(x)
ax.set_ylabel(y)
ax.set_title(z.replace('-',' ').title())
Um = integrate(X,Y,Z)/((X.max()-X.min())*(Y.max()-Y.min()))
txt = '$U_Q ={:1.3f}$'.format(Um)+' $[m \ s^{-1}]$'
ax.text(np.mean(ax.get_xlim()),np.mean(ax.get_ylim()),np.mean(ax.get_zlim()),txt,ha='center',va='center')