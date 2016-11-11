import pandas as pd
import hddm
import pickle

# load data
data = hddm.load_csv('Z://Work//UW//projects//RR_TMS//hddm//data//fullsplit_hddm.csv')

regm = hddm.HDDMRegressor(data, "z ~ rulert:C(tms, Treatment('NV'))", depends_on={'v': 'stim', 'a': 'stim'}, bias=True, include='all', p_outlier=0.05)
regm.find_starting_values()
regm.sample(2000, burn=200, dbname='Z://Work//UW//projects//RR_TMS//hddm//db//testmodel_traces.db', db='pickle')

fname = 'Z://Work//UW//projects//RR_TMS//hddm//models//by_cond//testmodel'
regm.save(fname)