import hddm

model = hddm.load('av_stim')

# init just a couple of vars
# conditions in DRI_TMS task
# inf/ins - X/Y
# sym/fin - S/F
# early/late/no stim - E/L/S
# PMd/Vertex stim - P/V

v_XFEP, v_XFEV, v_XFLP, v_XFLV, v_XFNP, v_XFNV, \
v_XSEP, v_XSEV, v_XSLP, v_XSLV, v_XSNP, v_XSNV, \
v_YFEP, v_YFEV, v_YFLP, v_YFLV, v_YFNP, v_YFNV, \
v_YSEP, v_YSEV, v_YSLP, v_YSLV, v_YSNP, v_YSNV = \
    model.nodes_db.node[['v( XFEP)', 'v( XFEV)', 'v( XFLP)', 'v( XFLV)', 'v( XFNP)', 'v( XFNV)',
                         'v( XSEP)', 'v( XSEV)', 'v( XSLP)', 'v( XSLV)', 'v( XSNP)', 'v( XSNV)',
                         'v( YFEP)', 'v( YFEV)', 'v( YFLP)', 'v( YFLV)', 'v( YFNP)', 'v( YFNV)',
                         'v( YSEP)', 'v( YSEV)', 'v( YSLP)', 'v( YSLV)', 'v( YSNP)', 'v( YSNV)']]

a_XFEP, a_XFEV, a_XFLP, a_XFLV, a_XFNP, a_XFNV, \
a_XSEP, a_XSEV, a_XSLP, a_XSLV, a_XSNP, a_XSNV, \
a_YFEP, a_YFEV, a_YFLP, a_YFLV, a_YFNP, a_YFNV, \
a_YSEP, a_YSEV, a_YSLP, a_YSLV, a_YSNP, a_YSNV = \
    model.nodes_db.node[['a( XFEP)', 'a( XFEV)', 'a( XFLP)', 'a( XFLV)', 'a( XFNP)', 'a( XFNV)',
                         'a( XSEP)', 'a( XSEV)', 'a( XSLP)', 'a( XSLV)', 'a( XSNP)', 'a( XSNV)',
                         'a( YFEP)', 'a( YFEV)', 'a( YFLP)', 'a( YFLV)', 'a( YFNP)', 'a( YFNV)',
                         'a( YSEP)', 'a( YSEV)', 'a( YSLP)', 'a( YSLV)', 'a( YSNP)', 'a( YSNV)']]

#z_XFEP, z_XFEV, z_XFLP, z_XFLV, z_XFNP, z_XFNV, \
#z_XSEP, z_XSEV, z_XSLP, z_XSLV, z_XSNP, z_XSNV, \
#z_YFEP, z_YFEV, z_YFLP, z_YFLV, z_YFNP, z_YFNV, \
#z_YSEP, z_YSEV, z_YSLP, z_YSLV, z_YSNP, z_YSNV = \
#    model.nodes_db.node[['z( XFEP)', 'z( XFEV)', 'z( XFLP)', 'z( XFLV)', 'z( XFNP)', 'z( XFNV)',
#                         'z( XSEP)', 'z( XSEV)', 'z( XSLP)', 'z( XSLV)', 'z( XSNP)', 'z( XSNV)',
#                         'z( YFEP)', 'z( YFEV)', 'z( YFLP)', 'z( YFLV)', 'z( YFNP)', 'z( YFNV)',
#                         'z( YSEP)', 'z( YSEV)', 'z( YSLP)', 'z( YSLV)', 'z( YSNP)', 'z( YSNV)']]

# plot the whole thang
hddm.analyze.plot_posterior_nodes([v_XFEP, v_XFEV, v_XFLP, v_XFLV, v_XFNP, v_XFNV,
                                   v_XSEP, v_XSEV, v_XSLP, v_XSLV, v_XSNP, v_XSNV,
                                   v_YFEP, v_YFEV, v_YFLP, v_YFLV, v_YFNP, v_YFNV,
                                   v_YSEP, v_YSEV, v_YSLP, v_YSLV, v_YSNP, v_YSNV])

hddm.analyze.plot_posterior_nodes([a_XFEP, a_XFEV, a_XFLP, a_XFLV, a_XFNP, a_XFNV,
                                   a_XSEP, a_XSEV, a_XSLP, a_XSLV, a_XSNP, a_XSNV,
                                   a_YFEP, a_YFEV, a_YFLP, a_YFLV, a_YFNP, a_YFNV,
                                   a_YSEP, a_YSEV, a_YSLP, a_YSLV, a_YSNP, a_YSNV])

hddm.analyze.plot_posterior_nodes([z_XFEP, z_XFEV, z_XFLP, z_XFLV, z_XFNP, z_XFNV,
                                   z_XSEP, z_XSEV, z_XSLP, z_XSLV, z_XSNP, z_XSNV,
                                   z_YFEP, z_YFEV, z_YFLP, z_YFLV, z_YFNP, z_YFNV,
                                   z_YSEP, z_YSEV, z_YSLP, z_YSLV, z_YSNP, z_YSNV])

# plot all inferred trials
hddm.analyze.plot_posterior_nodes([v_XFEP, v_XFEV, v_XFLP, v_XFLV, v_XFNP, v_XFNV,
                                   v_XSEP, v_XSEV, v_XSLP, v_XSLV, v_XSNP, v_XSNV])

hddm.analyze.plot_posterior_nodes([a_XFEP, a_XFEV, a_XFLP, a_XFLV, a_XFNP, a_XFNV,
                                   a_XSEP, a_XSEV, a_XSLP, a_XSLV, a_XSNP, a_XSNV])

hddm.analyze.plot_posterior_nodes([z_XFEP, z_XFEV, z_XFLP, z_XFLV, z_XFNP, z_XFNV,
                                   z_XSEP, z_XSEV, z_XSLP, z_XSLV, z_XSNP, z_XSNV])

#plot all instructed trials
hddm.analyze.plot_posterior_nodes([v_YFEP, v_YFEV, v_YFLP, v_YFLV, v_YFNP, v_YFNV,
                                   v_YSEP, v_YSEV, v_YSLP, v_YSLV, v_YSNP, v_YSNV])

hddm.analyze.plot_posterior_nodes([a_YFEP, a_YFEV, a_YFLP, a_YFLV, a_YFNP, a_YFNV,
                                   a_YSEP, a_YSEV, a_YSLP, a_YSLV, a_YSNP, a_YSNV])

hddm.analyze.plot_posterior_nodes([z_YFEP, z_YFEV, z_YFLP, z_YFLV, z_YFNP, z_YFNV,
                                   z_YSEP, z_YSEV, z_YSLP, z_YSLV, z_YSNP, z_YSNV])

# plot all symbol trials
hddm.analyze.plot_posterior_nodes([v_XSEP, v_XSEV, v_XSLP, v_XSLV, v_XSNP, v_XSNV,
                                   v_YSEP, v_YSEV, v_YSLP, v_YSLV, v_YSNP, v_YSNV])

hddm.analyze.plot_posterior_nodes([a_XSEP, a_XSEV, a_XSLP, a_XSLV, a_XSNP, a_XSNV,
                                   a_YSEP, a_YSEV, a_YSLP, a_YSLV, a_YSNP, a_YSNV])

hddm.analyze.plot_posterior_nodes([z_XSEP, z_XSEV, z_XSLP, z_XSLV, z_XSNP, z_XSNV,
                                   z_YSEP, z_YSEV, z_YSLP, z_YSLV, z_YSNP, z_YSNV])

# plot all finger trials
hddm.analyze.plot_posterior_nodes([v_XFEP, v_XFEV, v_XFLP, v_XFLV, v_XFNP, v_XFNV,
                                   v_YFEP, v_YFEV, v_YFLP, v_YFLV, v_YFNP, v_YFNV])

hddm.analyze.plot_posterior_nodes([a_XFEP, a_XFEV, a_XFLP, a_XFLV, a_XFNP, a_XFNV,
                                   a_YFEP, a_YFEV, a_YFLP, a_YFLV, a_YFNP, a_YFNV])

hddm.analyze.plot_posterior_nodes([z_XFEP, z_XFEV, z_XFLP, z_XFLV, z_XFNP, z_XFNV,
                                   z_YFEP, z_YFEV, z_YFLP, z_YFLV, z_YFNP, z_YFNV])

# plot all early stim trials
hddm.analyze.plot_posterior_nodes([v_XFEP, v_XFEV, v_XSEP, v_XSEV,
                                   v_YFEP, v_YFEV, v_YSEP, v_YSEV])
hddm.analyze.plot_posterior_nodes([a_XFEP, a_XFEV, a_XSEP, a_XSEV,
                                   a_YFEP, a_YFEV, a_YSEP, a_YSEV])
hddm.analyze.plot_posterior_nodes([z_XFEP, z_XFEV, z_XSEP, z_XSEV,
                                   z_YFEP, z_YFEV, z_YSEP, z_YSEV])

# plot all late stim trials
hddm.analyze.plot_posterior_nodes([v_XFLP, v_XFLV, v_XSLP, v_XSLV,
                                   v_YFLP, v_YFLV, v_YSLP, v_YSLV])
hddm.analyze.plot_posterior_nodes([a_XFLP, a_XFLV, a_XSLP, a_XSLV,
                                   a_YFLP, a_YFLV, a_YSLP, a_YSLV])
hddm.analyze.plot_posterior_nodes([z_XFLP, z_XFLV, z_XSLP, z_XSLV,
                                   z_YFLP, z_YFLV, z_YSLP, z_YSLV])

# plot all no stim trials
hddm.analyze.plot_posterior_nodes([v_XFNP, v_XFNV, v_XSNP, v_XSNV,
                                   v_YFNP, v_YFNV, v_YSNP, v_YSNV])
hddm.analyze.plot_posterior_nodes([a_XFNP, a_XFNV, a_XSNP, a_XSNV,
                                   a_YFNP, a_YFNV, a_YSNP, a_YSNV])
hddm.analyze.plot_posterior_nodes([z_XFNP, z_XFNV, z_XSNP, z_XSNV,
                                   z_YFNP, z_YFNV, z_YSNP, z_YSNV])

# plot all PMd trials
hddm.analyze.plot_posterior_nodes([v_XFEP, v_XFLP, v_XFNP,
                                   v_XSEP, v_XSLP, v_XSNP,
                                   v_YFEP, v_YFLP, v_YFNP,
                                   v_YSEP, v_YSLP, v_YSNP])
hddm.analyze.plot_posterior_nodes([a_XFEP, a_XFLP, a_XFNP,
                                   a_XSEP, a_XSLP, a_XSNP,
                                   a_YFEP, a_YFLP, a_YFNP,
                                   a_YSEP, a_YSLP, a_YSNP])
hddm.analyze.plot_posterior_nodes([z_XFEP, z_XFLP, z_XFNP,
                                   z_XSEP, z_XSLP, z_XSNP,
                                   z_YFEP, z_YFLP, z_YFNP,
                                   z_YSEP, z_YSLP, z_YSNP])

# plot all Vertex trials
hddm.analyze.plot_posterior_nodes([v_XFEV, v_XFLV, v_XFNV,
                                   v_XSEV, v_XSLV, v_XSNV,
                                   v_YFEV, v_YFLV, v_YFNV,
                                   v_YSEV, v_YSLV, v_YSNV])
hddm.analyze.plot_posterior_nodes([a_XFEV, a_XFLV, a_XFNV,
                                   a_XSEV, a_XSLV, a_XSNV,
                                   a_YFEV, a_YFLV, a_YFNV,
                                   a_YSEV, a_YSLV, a_YSNV])
hddm.analyze.plot_posterior_nodes([z_XFEV, z_XFLV, z_XFNV,
                                   z_XSEV, z_XSLV, z_XSNV,
                                   z_YFEV, z_YFLV, z_YFNV,
                                   z_YSEV, z_YSLV, z_YSNV])