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


COLOR_STYLE = ["red","green","blue","orange","violet","darkgreen"]
Y_LABEL = r"Hits in 2h"
X_LABEL = r"Energie in MeV"
X_START =0 
Y_START =0
X_END = 50000
Y_END = 35

X_MAJOR_TICK = 10000
Y_MAJOR_TICK = 5
X_MINOR_TICK = 2000
Y_MINOR_TICK = 1
SAVE_AS = "./RAD/plots/Höhenstrahlung.pdf"

path_ = "./RAD/RAD-Cosmic.xls"

data = getTableFromCells("C5","D1028",path_,"Höhenstrahlung")
kanalData = data.copy()
def calEnergie (Kanal):
    a = 48.8
    b = 8
    return a*Kanal+b

data = [calEnergie(np.array(data[0][100:])),data[1][100:]]

hunderterKanaele =[[],[]]
add = 0

for i in range (len(kanalData[0])):
    if i % 100 ==0:
        hunderterKanaele[0].append(kanalData[0][i])
        hunderterKanaele[1].append(add)
        add = 0
    add += kanalData[1][i]

totalEnergie = 0

for i in range(len(data[0])):
    totalEnergie += data[0][i] *  ufloat(data[1][i],np.sqrt(data[1][i]))



#printtableaslatex(np.transpose(np.array(hunderterKanaele)),"test1","test2")
print(totalEnergie)
totalEnergie = totalEnergie *1e3

result = totalEnergie * 1.60217e-19 / 1.24 / (2*3600) * 356*24*3600
print(result)

fig, ax = plt.subplots()


ax.grid()

ax.plot(data[0],data[1],color= COLOR_STYLE[0],label = "Höhenstrahlung")


ax.set_xlabel(X_LABEL)
ax.set_ylabel(Y_LABEL)
ax.set_xlim(X_START,X_END)
ax.set_ylim(Y_START,Y_END)
ax.legend()


# Define the formatter function
def format_func(value, tick_number):
    return round(value*1e-3,3)

# Set the x-axis formatter
ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_func))
ax.xaxis.set_major_locator(MultipleLocator(X_MAJOR_TICK))
ax.xaxis.set_minor_locator(MultipleLocator(X_MINOR_TICK))
ax.yaxis.set_major_locator(MultipleLocator(Y_MAJOR_TICK))
ax.yaxis.set_minor_locator(MultipleLocator(Y_MINOR_TICK))

plt.savefig(SAVE_AS)
plt.show()
