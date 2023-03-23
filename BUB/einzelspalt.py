
from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])
from AP import *
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from scipy import optimize
import matplotlib.ticker as ticker
from uncertainties.unumpy import *
from uncertainties import ufloat
import numpy as np

uncertanty = ufloat(5,0.1)/(ufloat(100,0.1)- ufloat(10,0.1))
print(uncertanty)

X_LABEL = r"Ordnung der Minima"
Y_LABEL = r"Verhältnis $\frac{s}{l}$"
X_START =0.5
Y_START =0
X_END = 5.5
Y_END = 0.02

X_MAJOR_TICK = 1
Y_MAJOR_TICK = 0.005
X_MINOR_TICK = 0.1e-4
Y_MINOR_TICK = 0.001
SAVE_AS = "./BUB/plots/einzelspalt.pdf"

path_ = "./BUB/BUB.xls"

data = getTableFromCells("C24","E29",path_,"Spalt")
print(data)
plotData = []
fitData = [[],[]]
for i in data:
    plotData.append([[1,2,3,4,5],[(i[j+1] /i[0]/2 )for j in range(len(i)-1)]])
    fitData[0].extend([1,2,3,4,5])
    fitData[1].extend([(i[j+1] /i[0]/2 )for j in range(len(i)-1)])

print(plotData)
#---------------  fit
# T = 22.7+273.15
def func(x,a,b):
    return a * x +b
def funcArr(n,arr):
    return func(n,arr[0],arr[1])


# popt,perr = optimize.curve_fit(func,data[0],data[1],p0=[1e-12,0])
# print(popt,np.sqrt(np.diag(perr)))
# fitDat =genDataFromFunktion(1000,0,3e-4,popt,funcArr)
fig, ax = plt.subplots()

l = [189.9,121.6,62.4]
ax.grid()
for i,I in enumerate(plotData):
    
    ax.errorbar(I[0],I[1],fmt="o",yerr=unumpy.std_devs(uncertanty),elinewidth=0.9,capsize=4,capthick=0.9,ecolor = "black",label = str(l[i]) + " cm")


popt,perr = optimize.curve_fit(func,fitData[0],fitData[1])
print(popt,np.sqrt(np.diag(perr)))
fitDat =genDataFromFunktion(10,X_START,X_END,popt,funcArr)
ax.plot(fitDat[0],fitDat[1],label=fr"Ausgleichsgerade")



# Set the x-axis formatter
# ax.yaxis.set_major_formatter(ticker.FuncFormatter(format_func))
ax.set_xlabel(X_LABEL)
ax.set_ylabel(Y_LABEL)
ax.set_xlim(X_START,X_END)
ax.set_ylim(Y_START,Y_END)
ax.legend()


ax.xaxis.set_major_locator(MultipleLocator(X_MAJOR_TICK))
ax.yaxis.set_major_locator(MultipleLocator(Y_MAJOR_TICK))


plt.savefig(SAVE_AS)
plt.show()


sl = ufloat(3.64e-3,0.13e-3)
lam = ufloat(532e-9,1e-9)
res = lam/sl
print(res)