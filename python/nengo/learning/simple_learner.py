# The basic simplest learning model
#doesn't learn super great

import nengo
import numpy as np

model = nengo.Network()
with model:
    
    #generates sinosoidal input
    stim = nengo.Node(lambda t: np.sin(t*2*np.pi))
    
    #represents input
    pre = nengo.Ensemble(n_neurons=100, dimensions=1)
    nengo.Connection(stim, pre)
    
    #population designated to learn input is initialized with a function that
    #returns zero - negates input signal
    post = nengo.Ensemble(n_neurons=100, dimensions=1)
    def init_func(x):
        return 0
    
    #define connection from pre to post that will be modified to "learn"
    #this connection doesn't connect error pop to post pop - it connects
    #error pop to the connection from pre to post
    learn_conn = nengo.Connection(pre, post, function=init_func,
                                  learning_rule_type=nengo.PES())
                                  
    #population to determine error between inout representation and post rep
    error = nengo.Ensemble(n_neurons=100, dimensions=1)
    
    #this is the function that will be encoded into the pre-post connection
    #implies that some other brain region already "knows" the function
    #(model-based learning) - implausible imo
    def desired_func(x):
        # adjust this to change what function is learned
        return x
    
    #connection from stim to error pop that inverts stim
    nengo.Connection(stim, error, function=desired_func, transform=-1)
    #connection between post pop and stim pop - inputs current post pop rep
    #into error pop
    nengo.Connection(post, error, transform=1)
    #connection between error pop and pre->post connection to be modified
    nengo.Connection(error, learn_conn.learning_rule)
    
    #flag to learn the input or not learn it
    stop_learn = nengo.Node(1)
    nengo.Connection(stop_learn, error.neurons, transform=-10*np.ones((100,1)))