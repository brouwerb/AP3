from uncertainties.unumpy import *
from uncertainties import ufloat
import numpy as np


from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])
from AP import *


path_ = "./OPA/OPA.xls"
Korrekturfakt = 0.51 # aus Student Tabelle
unsicherheit = 0.6

dataBl = getTableFromCells("A7","C11",path_,"N1")
Bl = ufloat(sum(dataBl[2])/5, Korrekturfakt * np.std(dataBl[2]) + unsicherheit)
print("Bl = ",Bl)
dataBk = getTableFromCells("A15","C19",path_,"N1")
Bk = ufloat(sum(dataBk[2])/5, Korrekturfakt * np.std(dataBk[2]) + unsicherheit)
print("Bk = ",Bk)
Bges = gewichteterMittelwert([Bl.nominal_value, Bk.nominal_value], [Bl.std_dev, Bk.std_dev])
Bgeserr = intExtFehler([Bl.nominal_value, Bk.nominal_value], [Bl.std_dev, Bk.std_dev])
print("Bges = ",ufloat(Bges, Bgeserr))

dataGl = getTableFromCells("D7","F11",path_,"N1")
Gl = ufloat(sum(dataGl[2])/5, Korrekturfakt * np.std(dataGl[2]) + unsicherheit)
print("Gl = ",Gl)
dataGk = getTableFromCells("D15","F19",path_,"N1")
Gk = ufloat(sum(dataGk[2])/5, Korrekturfakt * np.std(dataGk[2]) + unsicherheit)
print("Gk = ",Gk)
Gges = gewichteterMittelwert([Gl.nominal_value, Gk.nominal_value], [Gl.std_dev, Gk.std_dev])
Ggeserr = intExtFehler([Gl.nominal_value, Gk.nominal_value], [Gl.std_dev, Gk.std_dev])
print("Gges = ",ufloat(Gges, Ggeserr))




