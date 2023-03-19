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