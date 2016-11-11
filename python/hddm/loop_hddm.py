import pandas as pd
import hddm
import pickle

# load data
data = hddm.load_csv('Z://Work//UW//projects//RR_TMS//hddm//data//infins_hddm.csv')

# init models
models = []

# make models
for i in range(5):
    m = hddm.HDDM(data, depends_on={'v': 'stim', 'a': 'stim'})
    m.find_starting_values()
    m.sample(10000, burn=5000, dbname='Z://Work//UW//projects//RR_TMS//hddm//db//ii_va_stim_traces%i.db'%i, db='pickle')
    models.append(m)

# save models
for i in range(5):
    fname = 'Z://Work//UW//projects//RR_TMS//hddm//models//by_cond//ii_va_stim' + str(i)
    models[i].save(fname)


