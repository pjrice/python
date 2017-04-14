#a "mouse" that moves around
#if "scared", it returns "home" (starting position)


import nengo

model = nengo.Network()
with model:
    
    #stimulus that sets the desired position
    desired_direction_stim = nengo.Node([0,0])
    
    #population that represents the desired motion vector
    desired_direction = nengo.Ensemble(n_neurons=200, dimensions=2)
    nengo.Connection(desired_direction_stim, desired_direction)
    
    motor = nengo.Ensemble(n_neurons=200, dimensions=2)
    
    #nengo.Connection(desired_direction, motor)
    
    #population that represents the current position
    position = nengo.Ensemble(n_neurons=200, dimensions=2)
    nengo.Connection(motor, position, transform=0.05)
    nengo.Connection(position, position, synapse=0.1)
    
    #stimulus/pop that represents the amount of fear
    scared_stim = nengo.Node([0])
    scared = nengo.Ensemble(n_neurons=100, dimensions=1)
    nengo.Connection(scared_stim, scared)
    
    #population that takes desired direction vector and outputs it to motor if
    #not scared
    #if scared, tells motor to go home (start position)
    do_desired = nengo.Ensemble(n_neurons=500, dimensions=3)
    nengo.Connection(desired_direction, do_desired[:2])
    nengo.Connection(scared, do_desired[2])
    
    #function that determines whether to send direction vector or no signal
    #to motor
    def do_desired_func(x):
        desired_x, desired_y, scared = x
        if scared < 0.5:
            return desired_x, desired_y
        else:
            return 0, 0
    
    #connection to apply above func
    nengo.Connection(do_desired, motor, function=do_desired_func)
    
    #population to monitor position and fear
    do_home = nengo.Ensemble(n_neurons=500, dimensions=3)
    nengo.Connection(position, do_home[:2])
    nengo.Connection(scared, do_home[2])
    
    #function to send "home" signal to motor system if scared
    #returns negative of current position to force it through origin; when
    #it hits 0,0 returns 0,0 and holds position
    def do_home_func(x):
        pos_x, pos_y, scared = x
        if scared > 0.5:
            return -5*pos_x, -5*pos_y
        else:
            return 0, 0
    
    nengo.Connection(do_home, motor, function=do_home_func)
    