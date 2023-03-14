
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


COLOR_STYLE = ["red","green","blue","orange","violet","darkgreen"]
Y_LABEL = r"Zählrate"
X_LABEL = r"Wellenlänge $\lambda$ in $pm$"
X_START = 3.9e-11
Y_START =0
X_END = 8.5e-11
Y_END = 300

X_MAJOR_TICK = 0.5e-11
Y_MAJOR_TICK =50
X_MINOR_TICK = 0.1e-11
Y_MINOR_TICK = 10
SAVE_AS = "./XST/Plank.pdf"


path_ = "./XST/data.xls"

d = 0.5 * 564.02e-12
def angleToLambda(arrr):
    arr = arrr.copy()
    for i in range(len(arr)):
        arr[i] = 2* d *math.sin(math.radians(arr[i]))
    return arr


data = getTableFromCells("R5","X50",path_,"V5")
print (data)

def gerade (x,a,b):
    return a*x+b
def geradeArr (x,arr):
    return gerade(x,arr[0],arr[1])

L1 = [49,54.1,58.012,62.83,67.9,73.7]

fitData = []
for i,I in enumerate(L1):
    ind = getClosestPoint(L1[i],[[j* 1e12 for j in angleToLambda(data[0])],data[i+1]],getIndex=True)
    fitData.append([angleToLambda(data[0][ind:ind+5]),data[i+1][ind:ind+5]])
fitPlotData = []
schnittWerte = []
#print(fitData)
for i,I in enumerate(fitData):
    popt,perr = optimize.curve_fit(gerade,fitData[i][0],fitData[i][1],p0=[1e12,0])
    print(popt)
    schnittWerte.append(-popt[1]/popt[0])
    print(schnittWerte[-1]+10e-12)
    fitPlotData.append(genDataFromFunktion(100,schnittWerte[-1],schnittWerte[-1]+10e-12,popt,geradeArr))

#----------- plot

U = [35, 32.5, 30, 28, 26, 24]

fig, ax = plt.subplots()


ax.grid()
#print(angleToLambda(data[0]))
#ax.scatter(Totdat[0],Totdat[1],s=15)
for i in range(1,len(data)):
    arr = croppArray(data[0],data[i])
    xLamb =  angleToLambda(arr[0])
    ax.plot(xLamb,arr[1])
    ax.plot(fitPlotData[i-1][0],fitPlotData[i-1][1],color = "grey")#,label=fr"$\lambda_0$ = {schnittWerte[i-1] * 1e12} $pm$, U = {U[i-1]} kV")
    ax.plot([schnittWerte[i-1],schnittWerte[i-1]],[0,30],color=COLOR_STYLE[i-1],label= fr"$\lambda_0$ = {round(schnittWerte[i-1] * 1e12,2)} $pm$, U = {U[i-1]} kV")


ax.set_xlabel(X_LABEL)
ax.set_ylabel(Y_LABEL)
ax.set_xlim(X_START,X_END)
ax.set_ylim(Y_START,Y_END)



ax.xaxis.set_major_locator(MultipleLocator(X_MAJOR_TICK))
ax.xaxis.set_minor_locator(MultipleLocator(X_MINOR_TICK))
ax.yaxis.set_major_locator(MultipleLocator(Y_MAJOR_TICK))
ax.yaxis.set_minor_locator(MultipleLocator(Y_MINOR_TICK))

# Define the formatter function
def format_func(value, tick_number):
    return round(value*1e12,3)

# Set the x-axis formatter
ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_func))

plt.legend(loc=2,ncol=2)
plt.savefig(SAVE_AS)
plt.show()





