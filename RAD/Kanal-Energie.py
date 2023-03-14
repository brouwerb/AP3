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
Y_LABEL = r"Hits"
X_LABEL = r"Kanäle"
X_START =0 
Y_START =0
X_END = 850
Y_END = 2600

X_MAJOR_TICK = 100
Y_MAJOR_TICK =500
X_MINOR_TICK = 20
Y_MINOR_TICK = 100
SAVE_AS = "./RAD/plots/Kalibspektren.pdf"

path_ = "./RAD/RAD.xls"

elements = ["Cs-137","Co-60","Na-22"]

peaks = getTableFromCells("L4","O10",path_,"Kallibrierung")

print(peaks)


fig, ax = plt.subplots()


ax.grid()
fitData = []
for i,I in enumerate(peaks[1]):
    if peaks[3][i] != '':
        if peaks[0][i]== "Csäsium":
            Cs = ax.scatter(peaks[1][i],peaks[3][i],color = COLOR_STYLE[0])
        elif peaks[0][i]== "Cobalt":
            Co = ax.scatter(peaks[1][i],peaks[3][i],color = COLOR_STYLE[1])
        else:
            Na = ax.scatter(peaks[1][i],peaks[3][i],color = COLOR_STYLE[2])
        fitData.append([peaks[1][i],peaks[3][i]])

def gerade (x,a,b):
    return a*x+b
def geradeArr (x,arr):
    return gerade(x,arr[0],arr[1])

popt,perr = optimize.curve_fit(gerade,fitData[0],fitData[1])
fitPlot = genDataFromFunktion(5,X_START,X_END,popt,geradeArr)

fit = ax.plot(fitPlot[0],fitPlot[1],color="black")

ax.set_xlabel(X_LABEL)
ax.set_ylabel(Y_LABEL)
ax.set_xlim(X_START,X_END)
ax.set_ylim(Y_START,Y_END)
ax.legend([Cs,Co,Na,fit],elements.append("fit a"),loc=2)


ax.xaxis.set_major_locator(MultipleLocator(X_MAJOR_TICK))
ax.xaxis.set_minor_locator(MultipleLocator(X_MINOR_TICK))
ax.yaxis.set_major_locator(MultipleLocator(Y_MAJOR_TICK))
ax.yaxis.set_minor_locator(MultipleLocator(Y_MINOR_TICK))

plt.savefig(SAVE_AS)
plt.show()
