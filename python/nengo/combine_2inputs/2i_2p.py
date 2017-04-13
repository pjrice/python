#two inputs into one population with two dimensions
#2d pop inputs to 1d pop and performs function utilizing both initial dimesions

import nengo

model = nengo.Network()
with model:
    
    stim_a = nengo.Node([0])
    stim_b = nengo.Node([0])
    
    a = nengo.Ensemble(n_neurons=200, dimensions=2, radius=2)
    
    nengo.Connection(stim_a,a[0])
    nengo.Connection(stim_b,a[1])
    
    b = nengo.Ensemble(n_neurons=100,dimensions=1)
    
    def product(x):
        return x[0]*x[1]
        
    nengo.Connection(a,b,function=product)
