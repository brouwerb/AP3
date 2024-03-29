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
Y_LABEL = r"Hits in 400s"
X_LABEL = r"Kanäle"
X_START =0 
Y_START =0
X_END = 100
Y_END = 20000

X_MAJOR_TICK = 20
Y_MAJOR_TICK =2000
X_MINOR_TICK = 5
Y_MINOR_TICK = 500
SAVE_AS = "./RAD/plots/Cobalt-Höhen.pdf"

path_ = "./RAD/RAD-Cosmic.xls"

data = getTableFromCells("A5","B1028",path_,"Höhenstrahlung")




peaks = [24.0,27.0,51.2]




fig, ax = plt.subplots()


ax.grid()

ax.plot(data[0],data[1],color= COLOR_STYLE[0])

for i,I in enumerate(peaks):
    
    ax.axvline(I,color = "black",linewidth=0.8)




ax.set_xlabel(X_LABEL)
ax.set_ylabel(Y_LABEL)
ax.set_xlim(X_START,X_END)
ax.set_ylim(Y_START,Y_END)
ax.legend(("Cobalt","peaks"))


ax.xaxis.set_major_locator(MultipleLocator(X_MAJOR_TICK))
ax.xaxis.set_minor_locator(MultipleLocator(X_MINOR_TICK))
ax.yaxis.set_major_locator(MultipleLocator(Y_MAJOR_TICK))
ax.yaxis.set_minor_locator(MultipleLocator(Y_MINOR_TICK))

plt.savefig(SAVE_AS)
plt.show()
