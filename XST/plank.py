
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


#COLOR_STYLE = ["red","green","blue"]
Y_LABEL = r"Zählrate"
X_LABEL = r"Wellenlänge $\lambda$ in $pm$"
X_START = 3.9e-11
Y_START =0
X_END = 8.5e-11
Y_END = 250

X_MAJOR_TICK = 0.5e-11
Y_MAJOR_TICK =50
X_MINOR_TICK = 0.1e-11
Y_MINOR_TICK = 10
SAVE_AS = "./XST/Plank.pdf"


path_ = "./XST/data.xls"

d = 0.5 * 564.02e-12
def angleToLambda(arr):
    for i in range(len(arr)):
        arr[i] = 2* d *math.sin(math.radians(arr[i]))
    return arr


data = getTableFromCells("R5","X50",path_,"V5")

L0 = [4.7e-11,5.1e-11,5.55e-11,6.0e-11,6.57e-11,7.1e-11]

#----------- plot



fig, ax = plt.subplots()


ax.grid()
#print(angleToLambda(data[0]))
#ax.scatter(Totdat[0],Totdat[1],s=15)
for i in range(1,len(data)):
    arr = croppArray(data[0],data[i])
    xLamb =  angleToLambda(arr[0])
    ax.plot(xLamb,arr[1])
    clPoint = getClosestPoint(L0[i-1],[xLamb,arr[1]])
    ax.scatter(clPoint[0],clPoint[1],label=fr"$\lambda_0$ = {L0[i-1] * 1e12} $pm$")



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

plt.legend()
plt.savefig(SAVE_AS)
plt.show()




