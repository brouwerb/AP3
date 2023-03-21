
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



Y_LABEL = r"Ordnung der Minima"
X_LABEL = r"Winkel \alpha in °"
X_START =0 
Y_START =0
X_END = 3e-4+1
Y_END = 120000

X_MAJOR_TICK = 0.5e-4
Y_MAJOR_TICK =20000
X_MINOR_TICK = 0.1e-4
Y_MINOR_TICK = 5000
SAVE_AS = "./BUB/plots/einzelspalt.pdf"

path_ = "./BUB/BUB.xls"

data = getTableFromCells("C24","E29",path_,"Spalt")

plotData = []
for i in data:
    plotData.append([[1,2,3,4,5],[i[j+1] /i[0] for j in range(len(i)-1)]])


#---------------  fit
# T = 22.7+273.15
# def func(n,x,c):
#     return (n-c)*T*1/x
# def funcArr(n,arr):
#     return func(n,arr[0],arr[1])


# popt,perr = optimize.curve_fit(func,data[0],data[1],p0=[1e-12,0])
# print(popt,np.sqrt(np.diag(perr)))
# fitDat =genDataFromFunktion(1000,0,3e-4,popt,funcArr)


#ax.scatter(data[0],data[1],s=15)
ax.errorbar(np.array(data[0])-popt[1]+1,data[1],fmt="x",yerr=data[2], ecolor = 'black',elinewidth=0.9,capsize=4,capthick=0.9,label="Messdaten")
ax.plot(np.array(fitDat[0])-popt[1]+1,fitDat[1],color = "red",label=fr"fit mit $\chi$={round_errtex(popt[0],np.sqrt(np.diag(perr))[0])}" )



# Define the formatter function
def format_func(value, tick_number):
    return round(value*1e-3,3)

# Set the x-axis formatter
ax.yaxis.set_major_formatter(ticker.FuncFormatter(format_func))
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
