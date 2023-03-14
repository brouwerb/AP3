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
Y_END = 150

X_MAJOR_TICK = 500
Y_MAJOR_TICK =20
X_MINOR_TICK = 100
Y_MINOR_TICK = 5
SAVE_AS = "./RAD/plots/K2CO3.pdf"

path_ = "./RAD/RAD.xls"



def calEnergie (Kanal):
    a = 3.0352
    b = -27.1
    return a*Kanal+b


Untergrundraw = getTableFromCells("A4","D1027",path_,"Untergrund")
untergrund = [Untergrundraw[0],Untergrundraw[3]]

data  = getTableFromCells("A5","B1028",path_,"K2CO3")
data = [calEnergie(np.array(data[0])),np.array(data[1])-np.array(untergrund[1])]




fig, ax = plt.subplots()


ax.grid()

ax.plot(data[0],data[1],color= COLOR_STYLE[0],label = "K2CO3")
ax.axvline(calEnergie(484.9),label= f"peak bei {round_errtex(calEnergie(484.9),abs(calEnergie(8.7)))} KeV",color = "black")
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
