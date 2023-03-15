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
Y_LABEL = r"Hits in 10 min"
X_LABEL = r"Energie in KeV"
X_START =0 
Y_START =0
X_END = 2500
Y_END = 1500

X_MAJOR_TICK = 500
Y_MAJOR_TICK =200
X_MINOR_TICK = 100
Y_MINOR_TICK = 50
SAVE_AS = "./RAD/Plots/Untergrund.pdf"

path_ = "./RAD/RAD.xls"



def calEnergie (Kanal):
    a = 3.0352
    b = -27.1
    return a*Kanal+b


rawdata = getTableFromCells("A4","D1027",path_,"Untergrund")
data = [[calEnergie(i) for i in rawdata[0]],rawdata[1],rawdata[3]]

print(sum(data[1]), sum(data[2]), sum([data[0][i]*data[1][i] for i in range(len(data[1]))]), sum([data[0][i]*data[2][i] for i in range(len(data[1]))]))


fig, ax = plt.subplots()


ax.grid()
for i in range(len(data)-1):
    ax.plot(data[0],data[i+1],color= COLOR_STYLE[i])

ax.set_xlabel(X_LABEL)
ax.set_ylabel(Y_LABEL)
ax.set_xlim(X_START,X_END)
ax.set_ylim(Y_START,Y_END)
ax.legend(("Ohne Blei", "mit Blei"))


ax.xaxis.set_major_locator(MultipleLocator(X_MAJOR_TICK))
ax.xaxis.set_minor_locator(MultipleLocator(X_MINOR_TICK))
ax.yaxis.set_major_locator(MultipleLocator(Y_MAJOR_TICK))
ax.yaxis.set_minor_locator(MultipleLocator(Y_MINOR_TICK))

plt.savefig(SAVE_AS)
plt.show()
