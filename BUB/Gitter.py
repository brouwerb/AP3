
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



X_LABEL = r"Ordnung der Maxima"
Y_LABEL = r"Verhältnis $sin(arctan(\frac{s}{l}))$"
X_START =0.5
Y_START =0
X_END = 4.5
Y_END = 0.02

X_MAJOR_TICK = 1
Y_MAJOR_TICK = 0.005
X_MINOR_TICK = 0.1e-4
Y_MINOR_TICK = 0.001
SAVE_AS = "./BUB/plots/Gitter.pdf"

path_ = "./BUB/BUB.xls"

data = getTableFromCells("B34","M38",path_,"Gitter")

plotData = []
fitData = []
uncertanty =[]
colordif = [data[1:4],data[5:8],data[9:12]]
#print(colordif)
for h,H in enumerate(colordif):
    uncertanty.append([])
    plotData.append([])
    fitData.append([[],[]])
    for i in H:
        plotData[h].append([[1,2,3,4],[np.sin(np.arctan(i[j+1] /i[0]/2 ))for j in range(len(i)-1)]])
        fitData[h][0].extend([1,2,3,4])
        fitData[h][1].extend([np.sin(np.arctan(i[j+1] /i[0]/2 ))for j in range(len(i)-1)])
        uncertanty[h].append(unumpy.sin(unumpy.arctan(ufloat(i[-1],0.3)/(ufloat(i[0],0.2)))))

print(plotData)
print(fitData)
print(uncertanty)

#---------------  fit
# T = 22.7+273.15
def func(x,a,b):
    return a * x +b
def funcArr(n,arr):
    return func(n,arr[0],arr[1])


# popt,perr = optimize.curve_fit(func,data[0],data[1],p0=[1e-12,0])
# print(popt,np.sqrt(np.diag(perr)))
# fitDat =genDataFromFunktion(1000,0,3e-4,popt,funcArr)
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
fig3, ax3 = plt.subplots()

l = [79.85,26.15,52.6]
color = ["Grün","Blau","Rot"]


axes = [ax1,ax2,ax3]
figs = [fig1,fig2,fig3]
plt.xlabel(X_LABEL)
plt.ylabel(Y_LABEL)
for h,H in enumerate(plotData):
    for i,I in enumerate(H):
        axes[h].grid()
        axes[h].errorbar(I[0],I[1],fmt="o",yerr=unumpy.std_devs(uncertanty[h][i]),elinewidth=0.9,capsize=4,capthick=0.9,label = str(l[i]) + " cm")

    popt,perr = optimize.curve_fit(func,fitData[h][0],fitData[h][1])
    print(popt,np.sqrt(np.diag(perr)))
    fitDat =genDataFromFunktion(10,X_START,X_END,popt,funcArr)
    axes[h].plot(fitDat[0],fitDat[1],label=f"Ausgleichsgerade mit \n a={round_errtex(popt[0],np.sqrt(np.diag(perr))[0])}; b={round_errtex(popt[1],np.sqrt(np.diag(perr))[1])}")
    axes[h].legend(loc='upper left')
    figs[h].savefig(f"./BUB/plots/Gitter_{color[h]}.pdf")


# Set the x-axis formatter
# ax.yaxis.set_major_formatter(ticker.FuncFormatter(format_func))

plt.show()

sl = [ufloat(0.0549,0.0033),ufloat(0.0386,0.0042),ufloat(0.0574,0.0039)]
git = ufloat(10e-6,0.02e-6)
for i in sl:
    res = git * i
    print(res)