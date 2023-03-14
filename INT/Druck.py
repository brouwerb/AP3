
from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])
from AP import *
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from scipy import optimize
import matplotlib.ticker as ticker



Y_LABEL = r"Druck $\Delta p$ in Kpa"
X_LABEL = r"Brechungsindex $\Delta n$"
X_START =0 
Y_START =0
X_END = 2.5e-7
Y_END = 120000

X_MAJOR_TICK = 0.5e-7
Y_MAJOR_TICK =20000
X_MINOR_TICK = 0.1e-7
Y_MINOR_TICK = 5000
SAVE_AS = "./INT/plots/druck.pdf"

path_ = "./INT/INT.xls"

data = getTableFromCells("A16","B27",path_,"V2")

print(data)

lamb = 632.8e-9
laenge = 49.4
def cal_N(numMax):
    return numMax*lamb/2/laenge



#----------- plot

fig, ax = plt.subplots()


ax.grid()
data[0] = [cal_N(i) for i in data[0]]

data.append([(analogErr(0.02)+i*0.016)*1e5 for i in data[1]])
data[1] = [(1.0135-i)*1e5 for i in data[1]]
#print(data)

#---------------  fit
T = 22.7+273.15
def func(n,x,c):
    return n*T*1/x +c
def funcArr(n,arr):
    return func(n,arr[0],arr[1])


popt,perr = optimize.curve_fit(func,data[0],data[1],p0=[1e-12,0])
print(popt,np.sqrt(np.diag(perr)))
fitDat =genDataFromFunktion(1000,X_START,X_END,popt,funcArr)


#ax.scatter(data[0],data[1],s=15)
ax.errorbar(data[0],data[1],fmt="x",yerr=data[2], ecolor = 'black',elinewidth=0.9,capsize=4,capthick=0.9,label="Messdaten")
ax.plot(fitDat[0],fitDat[1],color = "red",label=fr"fit mit $\chi$={round_errtex(popt[0],np.sqrt(np.diag(perr))[0])}" )



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
