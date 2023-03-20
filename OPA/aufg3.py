from uncertainties.unumpy import *
from uncertainties import ufloat


from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])
from AP import *


path_ = "./OPA/OPA.xls"
Korrekturfakt = 0.51 # aus Student Tabelle
unsicherheit = 0.06*sqrt(2)
relativ = 0.0004
abstand_e = ufloat(64.7 -23.3, unsicherheit + relativ * (64.7 -23.3))

dataG = getTableFromCells("B8","D12",path_,"N2")
dG = ufloat(gewichteterMittelwert(dataG[2], [unsicherheit + relativ * i for i in dataG[2]]), intExtFehler(dataG[2], [unsicherheit + relativ * i for i in dataG[2]]))
brechG = 1/4 * (abstand_e-dG**2/abstand_e)
print(brechG)
abstand_e = ufloat(86.4,unsicherheit)- ufloat(23.3,unsicherheit)
print(abstand_e)
dataB = getTableFromCells("F8","H12",path_,"N2")
dB = ufloat(gewichteterMittelwert(dataB[2], [unsicherheit + relativ * i for i in dataB[2]]), intExtFehler(dataB[2], [unsicherheit + relativ * i for i in dataB[2]]))
brechB = 1/4 * (abstand_e-dB**2/abstand_e)
print(brechB)



