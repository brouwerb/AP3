
from AP import *
import matplotlib.pyplot as plt
COLOR_STYLE = ["red","green","blue"]
Y_LABEL = r"Zählrate"
X_LABEL = r"Winkel in $\circ$"

X_MAJOR_TICK = 1
SAVE_AS = "./XST/v1-3.pdf"


path = ".XST/data.xls"


data = [getAxis(4,i,237,path,"V4") for i in range(1,4)]

fig, ax = plt.subplots()

ax.set_xlabel(X_LABEL)
ax.set_ylabel(Y_LABEL)
ax.grid()
ax.plot(data[0],data[1])
ax.plot(data[0],data[2])

#plt.savefig(SAVE_AS)
plt.show()




