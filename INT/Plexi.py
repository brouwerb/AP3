
from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])
from AP import *
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from scipy import optimize
import matplotlib.ticker as ticker
import math



Y_LABEL = r"Anzahl Intensitätsmaxima"
X_LABEL = r"Winkel in $^\circ$"
X_START =-5
Y_START =0
X_END = 10.5
Y_END = 300

X_MAJOR_TICK = 2
Y_MAJOR_TICK =50
X_MINOR_TICK = 0.5
Y_MINOR_TICK = 10
SAVE_AS = "./INT/plots/plexi.pdf"

path_ = "./INT/INT.xls"

data = getTableFromCells("A5","B60",path_,"V3")


data[1] = [np.rad2deg(np.arctan((i-3.60)/28)) for i in data[1]]
data[0] = [-1*(i+230)+303 for i in data[0]]
print(data)
#---------------  fit
h = 19.46e-3
lamb= 632.8e-9
def func(a,n):
    return 2*h/lamb*(1-n-np.cos(np.deg2rad(a))+np.sqrt(np.power(n,2)-np.power(np.sin(np.deg2rad(a)),2)))



popt,perr = optimize.curve_fit(func,data[1],data[0],p0=[1])
print(popt,np.sqrt(np.diag(perr)))
fitDat =genDataFromFunktion(1000,X_START,X_END,popt,func)

fig, ax = plt.subplots()


ax.grid()

#ax.errorbar(data[0],data[1],fmt="x",yerr=data[2], ecolor = 'black',elinewidth=0.9,capsize=4,capthick=0.9,label="Messdaten")
ax.plot(fitDat[0],fitDat[1],color = "red",label=fr"fit mit n={round_err(popt[0],np.sqrt(np.diag(perr))[0])}" )
ax.scatter(data[1],data[0],s=15,label="Messdaten")



ax.set_xlabel(X_LABEL)
ax.set_ylabel(Y_LABEL)
ax.set_xlim(X_START,X_END)
ax.set_ylim(Y_START,Y_END)
ax.legend()


ax.xaxis.set_major_locator(MultipleLocator(X_MAJOR_TICK))
ax.xaxis.set_minor_locator(MultipleLocator(X_MINOR_TICK))
ax.yaxis.set_major_locator(MultipleLocator(Y_MAJOR_TICK))
ax.yaxis.set_minor_locator(MultipleLocator(Y_MINOR_TICK))

plt.savefig(SAVE_AS)
plt.show()
