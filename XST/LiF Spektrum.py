
from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])
from AP import *
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator



COLOR_STYLE = ["red","green","blue"]
Y_LABEL = r"Zählrate"
X_LABEL = r"Winkel in $^\circ$"
X_START =2
Y_START =0
X_END = 25
Y_END = 1800

X_MAJOR_TICK = 5
Y_MAJOR_TICK =500
X_MINOR_TICK = 1
Y_MINOR_TICK = 100
SAVE_AS = "./XST/LiF-Spektrum.pdf"


path_ = "./XST/data.xls"


data = [fillZeros(getAxis(4,i,235,path_,"V5")) for i in range(0,2)]
print(data)
fig, ax = plt.subplots()


ax.grid()

ax.plot(data[0],data[1])
ax.axvline(8.76,color="red",linewidth=0.8)
ax.axvline(9.9,color="green",linewidth=0.8)
ax.axvline(18.09,color="red",linewidth=0.8)
ax.axvline(20.41,color="green",linewidth=0.8)


ax.set_xlabel(X_LABEL)
ax.set_ylabel(Y_LABEL)
ax.set_xlim(X_START,X_END)
ax.set_ylim(Y_START,Y_END)

plt.legend(("LiF - Spektrum",r"$K_{\beta}$-Linie (8,76$^\circ$; 18,09$^\circ$)",r"$K_{\alpha}$-Linie (9,9$^\circ$; 20,41$^\circ$)"),loc=1)

ax.xaxis.set_major_locator(MultipleLocator(X_MAJOR_TICK))
ax.xaxis.set_minor_locator(MultipleLocator(X_MINOR_TICK))
ax.yaxis.set_major_locator(MultipleLocator(Y_MAJOR_TICK))
ax.yaxis.set_minor_locator(MultipleLocator(Y_MINOR_TICK))

plt.savefig(SAVE_AS)
plt.show()




