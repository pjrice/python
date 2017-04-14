#this accumulator has a sense of "urgency"
#value of "urgency" pushes evidence accumulated towards one boundary or the other

#the urgency allows this to "change it's mind", but the choice flag doesn't
#go down while evidence accumulates 

import nengo

model = nengo.Network()
with model:
    stim = nengo.Node([0])
    urgency = nengo.Node([0])
    
    acc = nengo.Ensemble(300, 3, radius=1.7, 
            noise=nengo.processes.WhiteSignal(period=10, high=100, rms=3))
    
    nengo.Connection(stim, acc[0])
    nengo.Connection(urgency, acc[2])
    
    def feedback(x):
        urgency = x[2]
        if x[0] + urgency> 0.9:
            return 1, 1
        elif x[0] - urgency < -0.9:
            return -1, 1
        elif x[1] > 0.5:
            if x[0] > 0:
                return 1, 1
            else:
                return -1, 1
        else:
            return x[0], 0
    
    nengo.Connection(acc, acc[:2], synapse=0.1, function=feedback)
    