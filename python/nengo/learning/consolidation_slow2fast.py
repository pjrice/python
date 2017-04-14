# Cortical consolidation
#Classical conditioning example was very slow
#use the slow process to learn a faster process over time

# If you have a slow, complex neural model with lots of internal steps,
# you may want to have its output be used to train up a fast system that
# directly approximates the desired function.

# Here, we have a slow mapping from pre->wm->target.  In this case, it is
# slow due to very long time constants, but in general this could also be
# something that requires a few steps through the basal ganglia or some other
# complex system.

# A direct connection from pre->post is trained using the error signal from
# the slow system.  It should learn to produce the correct output, and it
# will actually end up being faster than the original.

# You can change the function being computed by the slow system by adjusting
# the context slider.  If you change it, the fast system should learn the
# new function instead.

import nengo
import numpy as np

model = nengo.Network()
with model:
    
    #defines slow sinosoidal stimulus
    def stim_pulse(t):
        return np.sin(t)
        index = int(t / 1.0)
        values = [1, 0, -1, 0]
        return values[index % len(values)]
    pre_value = nengo.Node(stim_pulse)
    
    #define a slow synapse
    tau_slow = 0.2
    
    #defines pre, post, and target representation populations
    pre = nengo.Ensemble(100, 1)
    post = nengo.Ensemble(100, 1)
    target = nengo.Ensemble(100, 1)
    nengo.Connection(pre_value, pre)

    #init the connection from pre to post with a random function, to be modified
    conn = nengo.Connection(pre, post, function=lambda x: np.random.random(),
                learning_rule_type=nengo.PES())
    
    #init working memory pop
    wm = nengo.Ensemble(300, 2, radius=1.4)
    
    #init the context stimulus
    context = nengo.Node(1)
    #connect context stimulus to 2nd dimension of wm
    nengo.Connection(context, wm[1])
    #connect pre pop to wm with a slow synapse
    nengo.Connection(pre, wm[0], synapse=tau_slow)
    #connect wm to target pop with a slow synpase that multiplies the pre rep
    #by the context
    nengo.Connection(wm, target, synapse=tau_slow, 
                     function=lambda x: x[0]*x[1])
               
    #define error pop
    #error is post minus target
    error = nengo.Ensemble(n_neurons=100, dimensions=1)
    nengo.Connection(post, error, synapse=tau_slow*2, transform=1)
    nengo.Connection(target, error, transform=-1)
    
    #connect error pop to the pre->post connection
    nengo.Connection(error, conn.learning_rule)

    #flag to learn or not
    stop_learn = nengo.Node([1])
    nengo.Connection(stop_learn, error.neurons, transform=-10*np.ones((100,1)))
    
    #just a node to show both the target pop and the post pop rep
    both = nengo.Node(None, size_in=2)
    nengo.Connection(post, both[0], synapse=None)
    nengo.Connection(target, both[1], synapse=None)
    