from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])
from AP import *
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from scipy import optimize
import matplotlib.ticker as ticker


COLOR_STYLE = ["red","green","blue","orange","violet","darkgreen"]
Y_LABEL = r"Energie in KeV"
X_LABEL = r"Kanäle"
X_START =0 
Y_START =0
X_END = 60
Y_END = 2600

X_MAJOR_TICK = 10
Y_MAJOR_TICK =500
X_MINOR_TICK = 2
Y_MINOR_TICK = 100
SAVE_AS = "./RAD/plots/Cobalt-Kalib.pdf"

path_ = "./RAD/RAD.xls"

elements = ["Cs-137","Co-60","Na-22"]

peaks = [[24.0,27.0,51.2],[1173,1333,2506]]

print(peaks)


fig, ax = plt.subplots()


ax.grid()
fitData = [[],[]]
ax.scatter(peaks[0],peaks[1],color = COLOR_STYLE[0])




def gerade (x,a,b):
    return a*x+b
def geradeArr (x,arr):
    return gerade(x,arr[0],arr[1])

popt,perr = optimize.curve_fit(gerade,peaks[0],peaks[1],p0=[100,0])
print(popt,np.sqrt(np.diag(perr)))
fitPlot = genDataFromFunktion(5,X_START,X_END,popt,geradeArr)

fit, = ax.plot(fitPlot[0],fitPlot[1],color="black")

ax.set_xlabel(X_LABEL)
ax.set_ylabel(Y_LABEL)
ax.set_xlim(X_START,X_END)
ax.set_ylim(Y_START,Y_END)

ax.legend(("Co-60 peaks",f"fit ax+c mit a={round_errtex(popt[0],np.sqrt(np.diag(perr)[0]))}; b={round_errtex(popt[1],np.sqrt(np.diag(perr)[1]))}"),loc=2)


ax.xaxis.set_major_locator(MultipleLocator(X_MAJOR_TICK))
ax.xaxis.set_minor_locator(MultipleLocator(X_MINOR_TICK))
ax.yaxis.set_major_locator(MultipleLocator(Y_MAJOR_TICK))
ax.yaxis.set_minor_locator(MultipleLocator(Y_MINOR_TICK))

plt.savefig(SAVE_AS)
plt.show()
