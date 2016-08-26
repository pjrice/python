import hddm
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pickle

try:
    import IPython
    shell = IPython.get_ipython()
    shell.enable_matplotlib(gui='inline')
except:
    pass

i = int(input('Load which model? '))
param = input('Plot which parameter? (a, t, v, a_std) ')

model = hddm.load('Z://Work//UW//projects//RR_TMS//hddm//models//by_cond//va_stim%i'%i)

# stats = model.gen_stats()
# model.print_stats()

model.plot_posteriors(param)
