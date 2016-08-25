def run_model(id):
    import hddm
    import pickle
    import pandas as pd

    data = hddm.load_csv('C://python//hddm//data//full_hddm.csv')
    m = hddm.HDDM(data)
    m.find_starting_values()
    m.sample(5000, burn=20, dbname='C://python//hddm//db//db%i'%id, db='pickle')
    return m

from IPython.parallel import Client
v = Client()[:]
jobs = v.map(run_model, range(4))
models = jobs.get()


# gelman__rubin(models)

# Create a new model that has all traces concatenated of individual models.
# combined_model = kabuki.utils.concat_models(models)

