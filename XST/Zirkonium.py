
from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])
from AP import *
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import math


COLOR_STYLE = ["red","green","blue"]
Y_LABEL = r"Absorbtion $A$"
X_LABEL = r"Wellenlänge in $nm$"
X_START =0.04
Y_START =0.3
X_END = 0.1
Y_END = 1

X_MAJOR_TICK = 0.1e-1
Y_MAJOR_TICK =0.1
X_MINOR_TICK = 0.02e-1
Y_MINOR_TICK = 0.02
SAVE_AS = "./XST/Zirkonium.pdf"


path_ = "./XST/data.xls"


d = 0.5 * 564.02e-12
def angleToLambda(arr):
    for i in range(len(arr)):
        arr[i] = 2* d *math.sin(math.radians(arr[i]))
    return arr


data = [fillZeros(getAxis(5,i,236,path_,"V4")) for i in range(1,6)]

fig, ax = plt.subplots()
data[0] = angleToLambda(data[0])
print(data)
ax.grid()

ax.plot(np.array(data[0])*1e9,1-(np.array(data[3])/np.array(data[1])))
ax.axvline(0.0677,color="red",linewidth=0.8)
#ax.plot(data[0],data[3],color="orange")


ax.set_xlabel(X_LABEL)
ax.set_ylabel(Y_LABEL)
ax.set_xlim(X_START,X_END)
ax.set_ylim(Y_START,Y_END)

plt.legend(("Absorbtion",r"Absorptionskante bei 0.0677 $nm$"),loc = 1)

ax.xaxis.set_major_locator(MultipleLocator(X_MAJOR_TICK))
ax.xaxis.set_minor_locator(MultipleLocator(X_MINOR_TICK))
ax.yaxis.set_major_locator(MultipleLocator(Y_MAJOR_TICK))
ax.yaxis.set_minor_locator(MultipleLocator(Y_MINOR_TICK))

plt.savefig(SAVE_AS)
plt.show()




