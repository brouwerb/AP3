from uncertainties import ufloat, nominal_value
from uncertainties.umath import sin
#import uarray
from uncertainties.unumpy import uarray
import numpy as np
import uncertainties.unumpy as unp
from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])
from AP import *

# Constants
d = 564.02e-12 # Lattice spacing in meters
n_values = [1, 2, 3] # Orders of diffraction

# Angles in degrees with uncertainties
angles = arrToUnumpy([[6.4, 12.8, 19.55], [7.15, 14.5, 22.1]], 0.15)
data = angles
print(constructdata(angles))

# Convert angles to radians
angles = [np.pi*angle/180 for angle in np.transpose(angles)]

h = 6.62607004e-34
c = 299792458
e = 1.602176634e-19

# Calculate wavelengths for each angle and n value
wavelengths = []
Eg = []
for i, I in enumerate(angles):
    wavelength = (d * unp.sin(I)) / (i+1)
    wavelengths.append(wavelength*1e12)
    Eg.append(h*c/(wavelength*e*1000))
print(wavelengths)
# Average wavelengths over n values

avg_wavelengths = sum(wavelengths)/len(wavelengths)
print(avg_wavelengths)

#calc energy

E = h*c/(avg_wavelengths*e*1000)



data = [*data, *np.transpose(wavelengths), *np.transpose(Eg) ]
print(data)

printtableaslatex(constructdata(data), "Messwerte", ["$n = 1$", "$n = 2$", "$n = 3$"])

