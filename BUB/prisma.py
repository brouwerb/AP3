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
import numpy as np

phi = ufloat(124.1, analogErr(0.1))
theta = ufloat(4.1, analogErr(0.1))

winkel = uarray([48.2, 48.6, 50.4], (0.1)*np.sqrt(1/6.0))
wellen = uarray([578, 546.07, 435.83], [1, 0, 0])

e = (phi - theta)/2

print("e = ",e)
print("phi = ",phi)
print("theta = ",theta)

# n = \frac{\sin\left(\frac{d_{min} + e}{2}\right)}{\sin\left(\frac{e}{2}\right)}

def cal_n(w):
    return sin((w+e)/2)/sin(e/2)

n = [cal_n(w) for w in winkel]

for i in range(len(n)):
    print("n = ",n[i]," bei ",wellen[i],"nm" ,"winkel = ",winkel[i],"°")


#fit n with gerade with errors of n
def func(x,a,b):
    return a*x+b

popt, perr = optimize.curve_fit(func, nominal_values(wellen), nominal_values(n), sigma=std_devs(n), absolute_sigma=True)
err = np.sqrt(np.diag(perr))

print("a = ",ufloat(popt[0],err[0]))
print("b = ",ufloat(popt[1],err[1]))

data = np.linspace(400, 600, 1000)

#plot n with error
fig, ax = plt.subplots()
ax.grid()
ax.errorbar(nominal_values(wellen), nominal_values(n), xerr=std_devs(wellen), yerr=std_devs(n), fmt='o', label="Messwerte")
ax.plot(data, func(data, *popt), label=f"$n(\\lambda) = ${round_errtex(popt[0],err[0])}$ \\frac{{1}}{{\\mathrm{{nm}}}}\\cdot\\lambda + ${round_errtex(popt[1],err[1])}")
ax.set_xlabel(r"Wellenlänge $\lambda$ in nm")
ax.set_ylabel(r"Brechungsindex $n$")
ax.legend()

plt.savefig("./BUB/plots/prism1.pdf")
plt.show()

def wel(n):
    return (n-popt[1])/popt[0]

enerspar = np.array([48.7, 47.5])

ne = [cal_n(w) for w in enerspar]
le  = [wel(n) for n in ne]

for i in range(len(le)):
    print("Energie = ",enerspar[i],"°"," bei ",le[i],"nm", "n = ",ne[i])
