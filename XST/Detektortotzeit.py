
from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])
from AP import *
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from scipy import optimize
import matplotlib.ticker as ticker


#COLOR_STYLE = ["red","green","blue"]
Y_LABEL = r"Zählrate"
X_LABEL = r"Stromstärke in $mA$"
X_START =0 * 0.001
Y_START =0
X_END = 1.1 * 0.001
Y_END = 2200

X_MAJOR_TICK = 0.2 *0.001
Y_MAJOR_TICK =500
X_MINOR_TICK = 0.05 *0.001
Y_MINOR_TICK = 100
SAVE_AS = "./XST/Detektortotzeit.pdf"


path_ = "./XST/data.xls"


data = getTableFromCells("E5","O35",path_,"V5")
Totdat = [[i* 0.0001  for i in range(1,11)],[]]
Totdat[1] = [data[i][19] for i in range(1,11)]
print(Totdat)
#-------- curve fit
def func(x,r,t):
    return r * x *np.exp(-1*r*t*x)
def funcArr(x,arr):
    return func(x,arr[0],arr[1])

popt,perr = optimize.curve_fit(func,Totdat[0],Totdat[1])
print(popt,np.sqrt(np.diag(perr)))
fitDat =genDataFromFunktion(1000,X_START,X_END,popt,funcArr)



#----------- plot

fig, ax = plt.subplots()


ax.grid()

ax.scatter(Totdat[0],Totdat[1],s=15)
ax.errorbar(Totdat[0],Totdat[1],xerr=20e-6,fmt="x", ecolor = 'black',elinewidth=0.9,capsize=4,capthick=0.9,label="Messdaten")
ax.plot(fitDat[0],fitDat[1],color = "red")

ax.set_xlabel(X_LABEL)
ax.set_ylabel(Y_LABEL)
ax.set_xlim(X_START,X_END)
ax.set_ylim(Y_START,Y_END)


# Define the formatter function
def format_func(value, tick_number):
    return round(value*1000,2)

# Set the x-axis formatter
ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_func))

ax.xaxis.set_major_locator(MultipleLocator(X_MAJOR_TICK))
ax.xaxis.set_minor_locator(MultipleLocator(X_MINOR_TICK))
ax.yaxis.set_major_locator(MultipleLocator(Y_MAJOR_TICK))
ax.yaxis.set_minor_locator(MultipleLocator(Y_MINOR_TICK))



plt.legend(("Messwerte", fr"fit mit r={round_errtex(popt[0],np.sqrt(np.diag(perr))[0])}; $\tau$ = {round_errtex(popt[1],np.sqrt(np.diag(perr))[1])}"))
plt.savefig(SAVE_AS)
plt.show()




