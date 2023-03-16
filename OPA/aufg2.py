from uncertainties.unumpy import *
from uncertainties import ufloat


from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])
from AP import *


path_ = "./OPA/OPA.xls"
Korrekturfakt = 0.51 # aus Student Tabelle
unsicherheit = analogErr(1)

dataBl = getTableFromCells("A7","C11",path_,"N1")
Bl = ufloat(sum(dataBl[2])/5, Korrekturfakt * unsicherheit)
print("Bl = ",Bl)
dataBk = getTableFromCells("A15","C19",path_,"N1")
Bk = ufloat(sum(dataBk[2])/5, Korrekturfakt * unsicherheit)
print("Bk = ",Bk)
print("brech B = ", (Bl + Bk)/2)


dataGl = getTableFromCells("D7","F11",path_,"N1")
Gl = ufloat(sum(dataGl[2])/5, Korrekturfakt * unsicherheit)
print("Gl = ",Gl)
dataGk = getTableFromCells("D15","F19",path_,"N1")
Gk = ufloat(sum(dataGk[2])/5, Korrekturfakt * unsicherheit)
print("Gk = ",Gk)
print("brech G = ", (Gl + Gk)/2)



