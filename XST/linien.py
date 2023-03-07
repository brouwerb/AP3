from uncertainties import ufloat
from uncertainties.umath import sin
#import uarray
from uncertainties.unumpy import uarray
import numpy as np
import uncertainties.unumpy as unp
from AP.py import *

# Constants
d = 564.02e-12 # Lattice spacing in meters
n_values = [1, 2, 3] # Orders of diffraction

# Angles in degrees with uncertainties
angles = [[6.4, 12.8, 19.55], [7.15, 14.5, 22.1]]

# Convert angles to radians
angles = [np.pi*(uarray(angle, 0.15))/180 for angle in np.transpose(angles)]



# Calculate wavelengths for each angle and n value
wavelengths = []
for i, I in enumerate(angles):
    wavelength = (2 * d * unp.sin(I)) / (i+1)
    wavelengths.append(wavelength)
print(wavelengths)
# Average wavelengths over n values

avg_wavelengths = np.mean(wavelengths, axis=0)

print(avg_wavelengths)