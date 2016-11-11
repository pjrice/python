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

model = hddm.load('Z://Work//UW//projects//RR_TMS//hddm//models//by_cond//fullsplit%i'%i)

model.plot_posterior_predictive(figsize=(14,10))

print("Model DIC: %f"%model.dic)

model.plot_posterior_predictive()
plt.show()
plt.savefig('foo.pdf')