# Classical conditioning

#VERY slow learning

# There are three different unconditioned stimuli (US) that are provided
# to the model, one after the other.  Each has a different hardwired
# unconditioned response (UR).

# There is also a conditioned stimulus (CS) provided, and there is a different
# one for each US.  The model attempts to learn to trigger the correct
# conditioned response (CR) in response to the CS.  

# After learning, the CR should start to respond before the corresponding UR.

import nengo
import numpy as np

D = 3
N = D*50

model = nengo.Network(label="My Network")
with model:

    #one of the three dimensions deflects to 1 while t is between n.9 and n+1
    def us_stim(t):
        # cycle through the three US
        t = t % 3
        if 0.9 < t< 1: return [1, 0, 0]
        if 1.9 < t< 2: return [0, 1, 0]
        if 2.9 < t< 3: return [0, 0, 1]
        return [0, 0, 0]
    us_stim = nengo.Node(us_stim)

    #one of the three dimensions deflects to 1 while t is between n.7 and n+1
    #consequence is that cs stim begins slighly earlier than us stim and 
    #lasts through the duration of us stim
    def cs_stim(t):
        # cycle through the three CS
        t = t % 3
        if 0.7 < t< 1: return [1, 0, 0]
        if 1.7 < t< 2: return [0, 1, 0]
        if 2.7 < t< 3: return [0, 0, 1]
        return [0, 0, 0]
    
    cs_stim = nengo.Node(cs_stim)

    #init unconditioned stimulus representation population with N neurons 
    #representing D dimensions
    us = nengo.Ensemble(N, D)
    #init conditioned stimulus representation population with N*2 neurons 
    #representing D*2 dimensions
    cs = nengo.Ensemble(N*2, D*2)

    #connect us stimulus to first D-1 dimensions of us pop
    nengo.Connection(us_stim, us[:D])
    #connect cs stimulus to first D-1 dimensions of cs pop (pop is 2*D large)
    #NOT 2 dimensional - 2 times the number of dimensions
    nengo.Connection(cs_stim, cs[:D])
    #connect cs stim rep to last D dimensions of cs pop (pop is 2*D large) slowly
    nengo.Connection(cs[:D], cs[D:], synapse=0.2)

    #init unconditioned response representation population with N neurons 
    #representing D dimensions
    ur = nengo.Ensemble(N, D)
    #connect us pop to ur pop
    nengo.Connection(us, ur)
    
    #init conditioned response representation population with N neurons 
    #representing D dimensions
    cr = nengo.Ensemble(N, D)
    #init connection betwen cs pop and cr pop to be learned
    #I assume function collapses the 2*D rep of cs to 1*D rep of cr?
    learn_conn = nengo.Connection(cs, cr, function=lambda x: [0]*D)
    learn_conn.learning_rule_type = nengo.PES(learning_rate=3e-4)

    #init population representing error
    #error is the difference between the ur and the cr (cr-ur)
    error = nengo.Ensemble(N, D)
    #connect error to the cs->cr connection
    nengo.Connection(error, learn_conn.learning_rule)
    #flip the unconditioned response and send to error
    nengo.Connection(ur, error, transform=-1)
    #send conditioned response to error slowly
    nengo.Connection(cr, error, transform=1, synapse=0.1)

    #flag to start or stop learning
    stop_learn = nengo.Node([1])
    nengo.Connection(stop_learn, error.neurons, transform=-10*np.ones((N, 1)))