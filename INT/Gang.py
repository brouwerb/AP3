from uncertainties.unumpy import *
from uncertainties import ufloat

data = uarray([17.00, 33.30 - 17.00, 17.00, 33.40 - 17.00, 15.20, 32.60 - 15.29, 17.20, 34.00 - 17.20], 0.21)
l = ufloat(632.8, 0.1)*1e-9

g = 2500*l/(2*data)

gav = sum(g)/len(g)
print(gav)