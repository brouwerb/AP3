
from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])
from AP import *
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator



#COLOR_STYLE = ["red","green","blue"]
Y_LABEL = r"Zählrate"
X_LABEL = r"Winkel in $^\circ$"
X_START =8
Y_START =0
X_END = 11
Y_END = 2100

X_MAJOR_TICK = 1
Y_MAJOR_TICK =500
X_MINOR_TICK = 0.2
Y_MINOR_TICK = 100
SAVE_AS = "./XST/DetektortotzeitRoh.pdf"


path_ = "./XST/data.xls"


data = getTableFromCells("E5","O35",path_,"V5")
print(data)
fig, ax = plt.subplots()


ax.grid()

for i in range(len(data)-1):
    ax.plot(data[0],data[i+1])

ax.set_xlabel(X_LABEL)
ax.set_ylabel(Y_LABEL)
ax.set_xlim(X_START,X_END)
ax.set_ylim(Y_START,Y_END)

legende = [r"$I =$" + str(round(i* 0.1,2))+ r" $mA$" for i in range(1,11) ]
plt.legend((legende),loc=2)

ax.xaxis.set_major_locator(MultipleLocator(X_MAJOR_TICK))
ax.xaxis.set_minor_locator(MultipleLocator(X_MINOR_TICK))
ax.yaxis.set_major_locator(MultipleLocator(Y_MAJOR_TICK))
ax.yaxis.set_minor_locator(MultipleLocator(Y_MINOR_TICK))

plt.savefig(SAVE_AS)
plt.show()




