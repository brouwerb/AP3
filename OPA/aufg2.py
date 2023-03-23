from uncertainties.unumpy import *
from uncertainties import ufloat
import numpy as np


from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])
from AP import *


path_ = "./OPA/OPA.xls"
# Keine Student T verteilung sonder Tabelle 6 ABW Skript
unsicherheit = 0.06*sqrt(2)
relativ = 0.0004

dataBl = getTableFromCells("A7","C11",path_,"N1")
Bl = ufloat(gewichteterMittelwert(dataBl[2], [unsicherheit + relativ * i for i in dataBl[2]]), intExtFehler(dataBl[2], [unsicherheit + relativ * i for i in dataBl[2]]))
print("Bl = ",Bl)
dataBk = getTableFromCells("A15","C19",path_,"N1")
Bk = ufloat(gewichteterMittelwert(dataBk[2], [unsicherheit + relativ * i for i in dataBk[2]]), intExtFehler(dataBk[2], [unsicherheit + relativ * i for i in dataBk[2]]))
print("Bk = ",Bk)
Bges = gewichteterMittelwert([Bl.nominal_value, Bk.nominal_value], [Bl.std_dev, Bk.std_dev])
Bgeserr = intExtFehler([Bl.nominal_value, Bk.nominal_value], [Bl.std_dev, Bk.std_dev])
print("Bges = ",ufloat(Bges, Bgeserr))
Bgesu = ufloat(Bges, Bgeserr)

dataGl = getTableFromCells("D7","F11",path_,"N1")
Gl = ufloat(gewichteterMittelwert(dataGl[2], [unsicherheit + relativ * i for i in dataGl[2]]), intExtFehler(dataGl[2], [unsicherheit + relativ * i for i in dataGl[2]]))
print("Gl = ",Gl)
dataGk = getTableFromCells("D15","F19",path_,"N1")
Gk = ufloat(gewichteterMittelwert(dataGk[2], [unsicherheit + relativ * i for i in dataGk[2]]), intExtFehler(dataGk[2], [unsicherheit + relativ * i for i in dataGk[2]]))
print("Gk = ",Gk)
Gges = gewichteterMittelwert([Gl.nominal_value, Gk.nominal_value], [Gl.std_dev, Gk.std_dev])
Ggeserr = intExtFehler([Gl.nominal_value, Gk.nominal_value], [Gl.std_dev, Gk.std_dev])
Ggesu = ufloat(Gges, Ggeserr)

print("Gges = ",ufloat(Gges, Ggeserr))

path_ = "./OPA/OPA.xls"
Korrekturfakt = 0.51 # aus Student Tabelle
unsicherheit = 0.06*sqrt(2)
relativ = 0.0004
abstand_e = ufloat(64.7 -23.3, unsicherheit + relativ * (64.7 -23.3))
print("Abstand e = ",abstand_e)

dataG = getTableFromCells("B8","D12",path_,"N2")
dG = ufloat(gewichteterMittelwert(dataG[2], [unsicherheit + relativ * i for i in dataG[2]]), intExtFehler(dataG[2], [unsicherheit + relativ * i for i in dataG[2]]))
brechG = 1/4 * (abstand_e-dG**2/abstand_e)
print("Abstand G = ",dG)
print(brechG)
abstand_e = ufloat(86.4,unsicherheit)- ufloat(23.3,unsicherheit)

dataB = getTableFromCells("F8","H12",path_,"N2")
dB = ufloat(gewichteterMittelwert(dataB[2], [unsicherheit + relativ * i for i in dataB[2]]), intExtFehler(dataB[2], [unsicherheit + relativ * i for i in dataB[2]]))
brechB = 1/4 * (abstand_e-dB**2/abstand_e)
print("Abstand B = ",dB)
print(brechB)

gesamtB = ufloat(gewichteterMittelwert([brechB.nominal_value, Bges], [brechB.std_dev, Bgeserr]), intExtFehler([brechB.nominal_value, Bges], [brechB.std_dev, Bgeserr]))
gesamtG = ufloat(gewichteterMittelwert([brechG.nominal_value, Gges], [brechG.std_dev, Ggeserr]), intExtFehler([brechG.nominal_value, Gges], [brechG.std_dev, Ggeserr]))

print("Bges = ",gesamtB)

print("Gges = ",gesamtG)




