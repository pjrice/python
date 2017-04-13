#two inputs into one population with two dimensions
#2d pop inputs to 1d pop and performs function utilizing both initial dimesions

import nengo

model = nengo.Network()
with model:
    
    stim_a = nengo.Node([1])
    stim_b = nengo.Node([-1])
    
    a = nengo.Ensemble(n_neurons=300, dimensions=3, radius=2.2)
    
    def product(x):
        return x[0]*x[1]
        
    nengo.Connection(stim_a,a[0])
    nengo.Connection(stim_b,a[1])
    nengo.Connection(a[:2],a[2],function=product)

