from uncertainties.unumpy import *
from uncertainties import ufloat


from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])
from AP import *

from uncertainties import unumpy

def calculate_f_h(e, k, l, d):
    f = 0.5 * unumpy.sqrt((e - k - l)**2 - d**2)
    h = k + l - unumpy.sqrt((e - k - l)**2 - d**2)
    return f, h

def lengtherror(a):
    relative = 0.0004
    absolute = 0.06
    return uarray(a, absolute + relative * a)

path_ = "./OPA/OPA.xls"

datak = getTableFromCells("B16","D20",path_,"N3")
datal = getTableFromCells("F16","H20",path_,"N3")
datad = getTableFromCells("B5","D9",path_,"N3")

# Example usage
e = lengtherror(88) - lengtherror(23.2)
k = ufloat(gewichteterMittelwert(datak[2], [0.06 + 0.0004 * i for i in datak[2]]), intExtFehler(datak[2], [0.06 + 0.0004 * i for i in datak[2]]))
l = ufloat(gewichteterMittelwert(datal[2], [0.06 + 0.0004 * i for i in datal[2]]), intExtFehler(datal[2], [0.06 + 0.0004 * i for i in datal[2]]))
d = ufloat(gewichteterMittelwert(datad[2], [0.06 + 0.0004 * i for i in datad[2]]), intExtFehler(datad[2], [0.06 + 0.0004 * i for i in datad[2]]))

f_prime, h_prime = calculate_f_h(e, k, l, d)

<<<<<<< HEAD
=======
print(e, k, l, d)
>>>>>>> c1db1765f39811d14f28b3cde6b5e69e0118b8ab
print(f"f' = {f_prime}")
print(f"h' = {h_prime}")
