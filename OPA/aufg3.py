from uncertainties.unumpy import *
from uncertainties import ufloat


from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])
from AP import *


path_ = "./OPA/OPA.xls"
Korrekturfakt = 0.51 # aus Student Tabelle
unsicherheit = analogErr(0.1)
abstand_e = ufloat(64.7,unsicherheit)- ufloat(23.3,unsicherheit)

dataG = getTableFromCells("B8","D12",path_,"N2")
dG = ufloat(sum(dataG[2])/5, Korrekturfakt * unsicherheit)
brechG = 1/4 * (abstand_e-dG**2/abstand_e)
print(brechG)
abstand_e = ufloat(86.4,unsicherheit)- ufloat(23.3,unsicherheit)

dataB = getTableFromCells("F8","H12",path_,"N2")
dB = ufloat(sum(dataB[2])/5, Korrekturfakt * unsicherheit)
brechB = 1/4 * (abstand_e-dB**2/abstand_e)
print(brechB)



