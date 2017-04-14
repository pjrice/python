#implementation of an accumulator decision model in nengo
#acc accumulates information about stimulus
#choice deflects to 1 (aka choose alternative A) when some boundary in acc is reached
#choice deflects to -1 (aka choose alternative B) when some oppopsing boundary 
#in acc is reached

#acc contains noise

import nengo

model = nengo.Network()
with model:
    stim = nengo.Node([0])
    
    acc = nengo.Ensemble(50, 1, 
        noise=nengo.processes.WhiteSignal(period=10, high=100, rms=3))
    
    nengo.Connection(stim, acc)
    
    nengo.Connection(acc, acc, synapse=0.1)
    
    
    def do_choice(x):
        if x > 0.9: return 1
        if x < -0.9: return -1
        return 0
    choice = nengo.Ensemble(100, 1)
    nengo.Connection(acc, choice, function=do_choice)
    choice.intercepts = nengo.dists.Uniform(0.7,0.9)  