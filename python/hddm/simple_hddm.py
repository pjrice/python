import pandas as pd
import matplotlib.pyplot as plt
import hddm
import pickle

# Load data from csv file into a NumPy structured array
data = hddm.load_csv('C://python//hddm//data//simple_hddm.csv')

# Create a HDDM model multi object
model = hddm.HDDM(data)

# find a good starting point which helps with the convergence.
model.find_starting_values()

# Create model and start MCMC sampling
model.sample(2000, burn=20, dbname='traces.db', db='pickle')

# Print fitted parameters and other model statistics
model.save('C://python//hddm//models//simple//mymodel_jupyter')
