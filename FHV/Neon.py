from uncertainties.unumpy import *
from uncertainties import ufloat


from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])
from AP import *

from uncertainties import unumpy

path = "./FHV/FHV.xls"

rawdata = getTableFromCells("F8","G10",path,"Neon")
rawdata[0].pop()

data = rawdata[0] + rawdata[1]
print(data)

def uB(x):
    A = 0.005
    B = 8
    C = 0.1
    return [sqrt((A/100 * i / sqrt(3))**2 + (B**2 + 1) * (2*C / sqrt(3))**2) for i in x]


udatamean = ufloat(gewichteterMittelwert(data, uB(data)), intExtFehler(data, uB(data)))

print("Mittelwert Energie: ", udatamean)

h = 6.62607004 * 10**(-34)
c = 299792458
e = 1.602176634 * 10**(-19)

lamda = h * c / (udatamean*e)

print("Wellenlänge: ", lamda)