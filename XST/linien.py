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

Kbnom = [nominal_value(i[0]) for i in wavelengths]
Kberr = [std_dev(i[0]) for i in wavelengths]

Kbavg = gewichteterMittelwert(Kbnom, Kberr)
Kbavgerr = intExtFehler(Kbnom, Kberr)

print(round_errtex(Kbavg, Kbavgerr))

Kanom = [nominal_value(i[1]) for i in wavelengths]
Kaerr = [std_dev(i[1]) for i in wavelengths]

Kaavg = gewichteterMittelwert(Kanom, Kaerr)
Kaavgerr = intExtFehler(Kanom, Kaerr)

print(round_errtex(Kaavg, Kaavgerr))

avg_wavelengths = uarray([Kaavg, Kbavg], [Kaavgerr, Kbavgerr])

#calc energy

E = h*c/(avg_wavelengths*e*1000)

print(E)


data = [*data, *np.transpose(wavelengths), *np.transpose(Eg) ]
print(data)

printtableaslatex(constructdata(data), "Messwerte", ["$n = 1$", "$n = 2$", "$n = 3$"])

L = uarray([4.813165885397388e-11, 5.263708442320518e-11, 5.713021022715293e-11, 6.174982316236505e-11, 6.675139411337414e-11, 7.248380622946957e-11], 0.2e-11)

U0 = [35, 32.5, 30, 28, 26, 24]

U = uarray([35, 32.5, 30, 28, 26, 24], 0.5)*1000

e = 1.602176634e-19
c = 299792458

h = L * e * U / c
print([nominal_value(i) for i in h])

hav = gewichteterMittelwert([nominal_value(i) for i in h],[std_dev(i) for i in h])
herr = intExtFehler([nominal_value(i) for i in h],[std_dev(i) for i in h])
print(round_errtex(hav, herr))

