import hddm
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pickle

# load data
data = hddm.load_csv('Z://Work//UW//projects//RR_TMS//hddm//data//full_hddm.csv')

#make error RTs negative
def flip_ruleRTerrors(data):
    """Flip sign of ruleRT for lower boundary responses.

        :Arguments:
            data : numpy.recarray
                Input array with at least one column named 'RT' and one named 'response'
        :Returns:
            data : numpy.recarray
                Input array with RTs sign flipped where 'response' == 0

    """
    # Check if data is already flipped
    if np.any(data['rulert'] < 0):
        return data

    # Copy data
    data = pd.DataFrame(data.copy())

    # Flip sign for lower boundary response
    idx = data['response'] == 0
    data.ix[idx, 'rulert'] = -data.ix[idx, 'rulert']

    return data

data = hddm.utils.flip_errors(data)
data = flip_ruleRTerrors(data)

# plot RTs
fig = plt.figure()
ax = fig.add_subplot(111, xlabel='stimRT', ylabel='count', title='stimRT distributions')
for i, subj_data in data.groupby('subj_idx'):
    subj_data.rt.hist(bins=20, histtype='step')

fig1 = plt.figure()
ax1 = fig1.add_subplot(111, xlabel='ruleRT', ylabel='count', title='ruleRT distributions')
for i, subj_data in data.groupby('subj_idx'):
    subj_data.rt.hist(bins=20, histtype='step')







