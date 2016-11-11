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

model = hddm.load('Z://Work//UW//projects//RR_TMS//hddm//models//by_cond//fullsplit%i'%i)

v_Y, v_X = model.nodes_db.ix[["v_Intercept", "v_C(stim, Treatment('Y'))[T.X]"], 'node']

#v_XF, v_XS, v_YF, v_YS = model.nodes_db.ix[['v(XF)', 'v(XS)', 'v(YF)', 'v(YS)'], 'node']
#a_Int, a_EP, a_EV, a_LP, a_LV, a_NP, a_NV = model.nodes_db.ix[["a_Intercept",
#                                                              "a_rulert:C(tms, Treatment('NV'))[EP]",
#                                                               "a_rulert:C(tms, Treatment('NV'))[EV]",
#                                                               "a_rulert:C(tms, Treatment('NV'))[LP]",
#                                                               "a_rulert:C(tms, Treatment('NV'))[LV]",
#                                                               "a_rulert:C(tms, Treatment('NV'))[NP]",
#                                                               "a_rulert:C(tms, Treatment('NV'))[NV]"], 'node']

a_XF, a_XS, a_YF, a_YS = model.nodes_db.ix[['a(XF)', 'a(XS)', 'a(YF)', 'a(YS)'], 'node']
v_Int, v_EP, v_EV, v_LP, v_LV, v_NP, v_NV = model.nodes_db.ix[["v_Intercept",
                                                               "v_rulert:C(tms, Treatment('NV'))[EP]",
                                                               "v_rulert:C(tms, Treatment('NV'))[EV]",
                                                               "v_rulert:C(tms, Treatment('NV'))[LP]",
                                                               "v_rulert:C(tms, Treatment('NV'))[LV]",
                                                               "v_rulert:C(tms, Treatment('NV'))[NP]",
                                                               "v_rulert:C(tms, Treatment('NV'))[NV]"], 'node']

hddm.analyze.plot_posterior_nodes([v_Y, v_X])
plt.xlabel('drift-rate')
plt.ylabel('Posterior probability')
plt.title('Group mean posteriors of within-subject drift-rate effects.')

hddm.analyze.plot_posterior_nodes([v_XF, v_XS, v_YF, v_YS])
plt.xlabel('drift-rate')
plt.ylabel('Posterior probability')
plt.title('Group mean posteriors of within-subject drift-rate effects.')
plt.savefig('drift_rate.pdf')

hddm.analyze.plot_posterior_nodes([a_Int, a_EP, a_EV, a_LP, a_LV, a_NP, a_NV])
plt.xlabel('Distance between UB and LB')
plt.ylabel('Posterior probability')
plt.title('Group mean posteriors of within-subject boundary distance effects.')
plt.savefig('bdist.pdf')

######################################################################################################################

hddm.analyze.plot_posterior_nodes([a_XF, a_XS, a_YF, a_YS])
plt.xlabel('Distance between UB and LB')
plt.ylabel('Posterior probability')
plt.title('Group mean posteriors of within-subject boundary distance effects.')
plt.savefig('bdist.pdf')

hddm.analyze.plot_posterior_nodes([v_Int, v_EP, v_EV, v_LP, v_LV, v_NP, v_NV])
plt.xlabel('drift-rate')
plt.ylabel('Posterior probability')
plt.title('Group mean posteriors of within-subject drift-rate effects.')
plt.savefig('drift_rate.pdf')























