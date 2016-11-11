import hddm
import pandas as pd
import pickle


models = [];

for i in range(5):
    m = hddm.load('Z://Work//UW//projects//RR_TMS//hddm//models//by_cond//testmodel')
    models.append(m)

hddm.analyze.gelman_rubin(models)
