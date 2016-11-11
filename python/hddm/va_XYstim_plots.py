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

model = hddm.load('Z://Work//UW//projects//RR_TMS//hddm//models//by_cond//ii_vreg_stim%i'%i)

v_X, v_Y =  model.nodes_db.node[['v(X)', 'v(Y)']]
a_X, a_Y =  model.nodes_db.node[['a(X)', 'a(Y)']]

hddm.analyze.plot_posterior_nodes([v_X, v_Y])
hddm.analyze.plot_posterior_nodes([a_X, a_Y])