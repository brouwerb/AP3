from uncertainties.unumpy import *
from uncertainties import ufloat


from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])
from AP import *



import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import unumpy

plt.rcParams['text.usetex'] = True

def func_g(beta, f, h1):
    return f * (1 - 1 / beta) + h1

def func_g_prime(beta, f_prime, h2):
    return f_prime * (1 - beta) + h2

def lengtherror(a):
    relative = 0.0004
    absolute = 0.06
    return uarray(a, [absolute + relative * i for i in a])

path_ = "./OPA/OPA.xls"

data = getTableFromCells("B5","F17",path_,"N4")

e = lengtherror(data[0])-20
s1 = lengtherror(data[1])-20
s2 = lengtherror(data[2][4:])-20
beta1 = -uarray(data[3], 0.2)/ufloat(5, 0.2)
beta2 = -uarray(data[4][4:], 0.2)/ufloat(5, 0.2)

e = np.concatenate((e, e[4:]))

# Example data with uncertainties
beta = np.concatenate((beta1, beta2))
g = -np.concatenate((s1, s2))

# Extract nominal values and standard deviations from uarrays
beta_nom = unumpy.nominal_values(beta)
beta_std = unumpy.std_devs(beta)
g_nom = unumpy.nominal_values(g)
g_std = unumpy.std_devs(g)

# Fit data to function g
popt_g , pcov_g = curve_fit(func_g,beta_nom,g_nom,sigma=g_std)

# calculate errors
errors_g = np.sqrt(np.diag(pcov_g))

# Print results

print(f"f = {popt_g[0]} +- {errors_g[0]}")
print(f"h1 = {popt_g[1]} +- {errors_g[1]}")

# Plot data with error bars and fitted function
plt.errorbar(g_nom,(1-1/beta_nom),xerr=g_std,fmt='o',label='Messwerte')
plt.plot(func_g(np.linspace(np.min(beta_nom), np.max(beta_nom)) ,*popt_g),(1-1/np.linspace(np.min(beta_nom), np.max(beta_nom))) ,label=f"Fit g mit $f = {round_errtex(popt_g[0],errors_g[0])}$ and $h_1 = {round_errtex(popt_g[1],errors_g[1])}$")
# axis labels
plt.xlabel('g in cm')
plt.ylabel(r"$1 - \frac{1}{\beta}$")
plt.legend()
plt.savefig("OPA/g.pdf")
plt.show()



beta_nom = unumpy.nominal_values(beta)
beta_std = unumpy.std_devs(beta)
g_nom = unumpy.nominal_values(e+g)
g_std = unumpy.std_devs(e+g)

# Fit data to function g_prime
popt_g_prime , pcov_g_prime = curve_fit(func_g_prime,beta_nom,g_nom,sigma=g_std)

# calculate errors
errors_g_prime = np.sqrt(np.diag(pcov_g_prime))

# Print results

print(f"f_prime = {popt_g_prime[0]} +- {errors_g_prime[0]}")
print(f"h2 = {popt_g_prime[1]} +- {errors_g_prime[1]}")
favg = gewichteterMittelwert([popt_g[0], -popt_g_prime[0]],[errors_g[0],errors_g_prime[0]])
favgerr = intExtFehler([popt_g[0], -popt_g_prime[0]],[errors_g[0],errors_g_prime[0]])

print(f"f_avg = {favg} +- {favgerr}")

# Plot data mit error bars and fitted function
plt.errorbar(g_nom,1-beta_nom,xerr=g_std,yerr=beta_std, fmt='o',label='Messwerte')
plt.plot(func_g_prime(np.linspace(np.min(beta_nom), np.max(beta_nom)) ,*popt_g_prime),1 - np.linspace(np.min(beta_nom), np.max(beta_nom)) ,label=f"Fit g' with $f' = {round_errtex(popt_g_prime[0],errors_g_prime[0])}$ and $h_2 = {round_errtex(popt_g_prime[1],errors_g_prime[1])}$")
# axis labels
plt.xlabel("g' in cm")
plt.ylabel(r"$1 - \beta$")
plt.legend()
plt.savefig("OPA/g_prime.pdf")
plt.show()
