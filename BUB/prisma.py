from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])
from AP import *
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from scipy import optimize
import matplotlib.ticker as ticker
from uncertainties.unumpy import *
from uncertainties import ufloat
import numpy as np

phi = ufloat(124.1, analogErr(0.1))
theta = ufloat(4.1, analogErr(0.1))

e = (phi - theta)/2

print("e = ",e)