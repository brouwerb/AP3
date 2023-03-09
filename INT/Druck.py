
from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])
from AP import *
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from scipy import optimize
import matplotlib.ticker as ticker



Y_LABEL = r"Zählrate"
X_LABEL = r"Stromstärke in $mA$"
X_START =0 
Y_START =0
X_END = 2.5e-7
Y_END = 2200

X_MAJOR_TICK = 0.2 *0.001
Y_MAJOR_TICK =500
X_MINOR_TICK = 0.05 *0.001
Y_MINOR_TICK = 100
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

data.append([(analogErr(0.02)+i*0.016)*1e-5 for i in data[1]])
data[1] = [(1.0135-i)*1e-5 for i in data[1]]
#print(data)

#---------------  fit
T = 22.7+273.15
def func(n,x,c):
    return n*T*1/x +c
def funcArr(n,arr):
    return func(n,arr[0],arr[1])


popt,perr = optimize.curve_fit(func,data[0],data[1])
print(popt,np.sqrt(np.diag(perr)))
fitDat =genDataFromFunktion(1000,X_START,X_END,popt,funcArr)


#ax.scatter(data[0],data[1],s=15)
err2 =ax.errorbar(data[0],data[1],fmt="x",yerr=data[2], ecolor = 'black',elinewidth=0.9,capsize=4,capthick=0.9)
ax.plot(fitDat[0],fitDat[1],color = "red")

plt.savefig(SAVE_AS)
plt.show()
