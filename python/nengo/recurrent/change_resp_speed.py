#change the speed of an input with a recurrent connection

import nengo

model = nengo.Network()
with model:
    stim = nengo.Node([0])
    
    a = nengo.Ensemble(n_neurons=100, dimensions=1)
    
    #a synapse that slows response to input by a factor of 10
    #the recurrent connection does nothing with desired_filter set to 1
    actual_synapse = 0.1
    #desired_filter = 1
    
    #decreasing the value of the filter speeds the response of the population up
    #but, it also introduces noise into the signal at a certain level
    #desired_filter = 0.5
    #desired_filter = 0.05
    desired_filter = 0.005
    #noisy here with little to no gain in speed
    #desired_filter = 0.0005
    
    def forward(x):
        return (actual_synapse/desired_filter) * x
    
    nengo.Connection(stim, a, function=forward,
                     synapse=actual_synapse)
    
    def recurrent(x):
        return (1-actual_synapse/desired_filter)*x
    
    
    nengo.Connection(a,a, function=recurrent,
                       synapse=actual_synapse)
