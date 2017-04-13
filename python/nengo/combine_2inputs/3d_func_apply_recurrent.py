#two inputs into one population with three dimensions
#first two dimensions input to third through recurrent connection and perform
#function

import nengo

model = nengo.Network()
with model:
    
    stim_a = nengo.Node([0])
    stim_b = nengo.Node([0])
    
    a = nengo.Ensemble(n_neurons=200, dimensions=3, radius=2)
    
    nengo.Connection(stim_a,a[0])
    nengo.Connection(stim_b,a[1])
    
    def product(x):
        return x[0]*x[1]

    nengo.Connection(a[:2],a[2],function=product)