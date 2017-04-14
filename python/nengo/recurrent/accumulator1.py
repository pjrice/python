#this accumulator population also represents the fact that choice has been made
#first dimension is evidence accumulation, second is choice "flag"
#is "sticky" about the decision - will not deflect once boundary reached unless reset
#also safeguards against slow evidence accumulation - 

import nengo

model = nengo.Network()
with model:
    stim = nengo.Node([0])

    acc = nengo.Ensemble(300, 2, radius=1.5, 
            noise=nengo.processes.WhiteSignal(period=10, high=100, rms=3))
    
    nengo.Connection(stim, acc[0], transform=0.1)

    def feedback(x):
        #if x[0] has accumulated evidence to boundary, return the boundary reached
        #and the choice flag
        if x[0]> 0.9:
            return 1, 1
        elif x[0]< -0.9:
            return -1, 1
        #once choice has been made, keep decision at boundary and choice flag up
        elif x[1] > 0.5:
            if x[0] > 0:
                return 1, 1
            else:
                return -1, 1
        #else return the evidence accumulated so far, and don't throw choice flag
        else:
            return x[0], 0
    
    nengo.Connection(acc, acc, synapse=0.1, function=feedback)
    