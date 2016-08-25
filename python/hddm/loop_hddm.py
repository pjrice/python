import pandas as pd
import hddm
import pickle

# load data
data = hddm.load_csv('C://python//hddm//data//full_hddm.csv')

# init models
models = []

# make models
for i in range(5):
    m = hddm.HDDM(data, depends_on={'v': 'stim', 'a': 'stim'})
    m.find_starting_values()
    m.sample(10000, burn=5000, dbname='C://python//hddm//db//va_stim_traces%i.db'%i, db='pickle')
    models.append(m)

# save models
for i in range(5):
    fname = 'C://python//hddm//models//by_cond//va_stim' + str(i)
    models[i].save(fname)


