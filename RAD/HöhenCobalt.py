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
Y_LABEL = r"Hits in 60s"
X_LABEL = r"Kanäle"
X_START =0 
Y_START =0
X_END = 850
Y_END = 14000

X_MAJOR_TICK = 100
Y_MAJOR_TICK =2000
X_MINOR_TICK = 20
Y_MINOR_TICK = 500
SAVE_AS = "./RAD/plots/Kalibspektren.pdf"

path_ = "./RAD/RAD-Cosmic.xls"

rawdata = getTableFromCells("A5","G1028",path_,"Kallibrierung")
data = [rawdata[0],rawdata[1],rawdata[3],rawdata[6]]

elements = ["Cs-137","Co-60","Na-22"]

peaks = getTableFromCells("L4","N10",path_,"Kallibrierung")




fig, ax = plt.subplots()


ax.grid()
for i in range(len(data)-1):
    ax.plot(data[0],data[i+1],label = elements[i],color= COLOR_STYLE[i])
for i,I in enumerate(peaks[1]):
    if i == 0:
        ax.axvline(I,color = "black",label = "peaks",linewidth=0.8)
    else:
        ax.axvline(I,color = "black",linewidth=0.8)




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
