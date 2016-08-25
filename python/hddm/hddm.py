import pandas as pd
import hddm
import pickle

# load data
data = hddm.load_csv('C://python//hddm//data//full_hddm.csv')

model = hddm.HDDM(data, depends_on={'v': 'stim', 'a': 'stim', 'z': 'stim'})
model.find_starting_values()
model.sample(2000, burn=20, dbname='C://python//hddm//db//avz_stim_traces.db', db='pickle')

model.save('C://python//hddm//models//by_cond//avz_stim')
