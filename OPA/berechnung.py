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

# $f_G = 7.492(31) \si{\centi\metre}$ und $f' = 13,10(20) \si{\centi\metre}$ berechnet werden. Der Abstand $t = 3 \si{\centi\metre}$ ist auch gegeben.

fg = ufloat(7.492, 0.031)
fprime = -ufloat(13.10, 0.20)
t = ufloat(3, 0.1)

# f_E = \frac{f' \left(t - f'\right)}{f' - f_G}

fe = (fprime * (t - fprime)) / (fprime - fg)

print(round_errtexU(fe))

# f = -14.217358712948112 +- 0.2731205004678588
# h1 = 6.805545776387112 +- 0.7358039549143498
# f_prime = 12.740920843838177 +- 0.1891303597826986
# h2 = 6.827218313718756 +- 0.8698094859938467

f = ufloat(-14.217358712948112, 0.2731205004678588)
h1 = ufloat(6.805545776387112, 0.7358039549143498)
fprime = ufloat(12.740920843838177, 0.1891303597826986)
h2 = ufloat(6.827218313718756, 0.8698094859938467)
f_1 = -10
f_2 = fg

# z &= \frac{f_1 \cdot t}{t - f_1' - f_2'}  \\
#         z' &= \frac{f_2 \cdot t}{t - f_1' - f_2'} \\
#         h &= \frac{t}{t - f_1' - f_2'}

z = (-f_1 * t) / (t - f_1 - f_2)
zprime = (f_2 * t) / (t - f_2 - f_1)
h = t / (t - f_1 - f_2)


print(round_errtexU(z))
print(round_errtexU(zprime))
print(round_errtexU(h))