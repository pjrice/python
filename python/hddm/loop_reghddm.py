import pandas as pd
import hddm
import pickle

# load data
data = hddm.load_csv('Z://Work//UW//projects//RR_TMS//hddm//data//fullsplit_hddm.csv')

# init models
regmodels = []

# make models
# hddm.HDDMRegressor(data, "v ~ C(stim, Treatment('Y'))")  |||  filename: ii_vreg_stim
# hddm.HDDMRegressor(data, "a ~ rulert:C(tms, Treatment('NV'))", depends_on={'v': 'stim'})  |||  filename: fullsplit
# hddm.HDDMRegressor(data, "v ~ rulert:C(tms, Treatment('NV'))", depends_on={'a': 'stim'})  |||  filename: fullsplit_vaswap
# hddm.HDDMRegressor(data, "z ~ rulert:C(tms, Treatment('NV'))", depends_on={'v': 'stim', 'a': 'stim'}, bias=True, include='all', p_outlier=0.05)  |||  filename: fullsplit_both
for i in range(5):
    regm = hddm.HDDMRegressor(data, "z ~ rulert:C(tms, Treatment('NV'))", depends_on={'v': 'stim', 'a': 'stim'}, bias=True, include='all', p_outlier=0.05)
    regm.find_starting_values()
    regm.sample(10000, burn=5000, dbname='Z://Work//UW//projects//RR_TMS//hddm//db//fullsplit_both_traces%i.db'%i, db='pickle')
    regmodels.append(regm)

# save models
for i in range(5):
    fname = 'Z://Work//UW//projects//RR_TMS//hddm//models//by_cond//fullsplit_both' + str(i)
    regmodels[i].save(fname)