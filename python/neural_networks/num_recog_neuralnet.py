# A Feedforward neural network solving the XOR problem with backprop.
import numpy as np  # Fast math and arrays
import matplotlib.pyplot as plt  # Displays


#show the number that was loaded
#num = np.loadtxt("7.txt") # Load the corresponding file , 1...9.txt

num1 = np.loadtxt("1.txt")
num2 = np.loadtxt("2.txt")
num3 = np.loadtxt("3.txt")
num4 = np.loadtxt("4.txt")
num5 = np.loadtxt("5.txt")
num6 = np.loadtxt("6.txt")
num7 = np.loadtxt("7.txt")
num8 = np.loadtxt("8.txt")
num9 = np.loadtxt("9.txt")
nums = np.stack((num1,num2,num3,num4,num5,num6,num7,num8,num9))

patterns = nums

num = nums[np.random.randint(1,9)]

n_input  = num.size
n_hidden = 5
n_output = 9

x = np.zeros((n_input))   # Input values
w1 = (np.random.random((n_input, n_hidden)) / 5) - 0.1    # First layer of synapses
h  = np.zeros((1, n_hidden))                              # Hidden layer
w2 = (np.random.random((n_hidden, n_output)) / 5) - 0.1   # Second layer of synapses

eta = 2.0   # Learning rate. This is higher than usual.

# The patterns to learn

#patterns = [[0, 0], [0, 1], [1, 0], [1, 1]]
#load numbers into array here

# Redefining some crucial functions

#activation function - transforms layer's input into layer's activation
def logistic(x, deriv = False):
    """Sigmoid logistic function (with derivative)"""
    if deriv:
        return x * (1 - x)
    else:
        return 1 / (1 + np.exp(-x))

    
def set_inputs(vals):
    """Sets a given XOR pattern into the input value"""
    global x
    x = np.reshape(vals,28,1)
    
    
def activation():
    """Spreads activation through a network"""
    global h
    
    # First pass, from input to hidden layer
    h_input = np.dot(x, w1)
    h = logistic(h_input)
    
    # Second pass, from hidden layer to output
    output_input = np.dot(h, w2)
    return logistic(output_input)
    
def calculate_response(digit):
    """Calculates the response of the neuron to a digit"""
    set_inputs(digit)
    return activation()
    
def error(i, response):
    """Calculates the error function"""
    return 0.5 * np.sum((target(i) - response) ** 2)


def target(val):
    """Desired response function, t(p)"""
    if  np.all(val == num1):
        return [1,0,0,0,0,0,0,0,0]   
    elif np.all(val == num2):
        return [0,1,0,0,0,0,0,0,0]
    elif np.all(val == num3):
        return [0,0,1,0,0,0,0,0,0]
    elif np.all(val == num4):
        return [0,0,0,1,0,0,0,0,0]
    elif np.all(val == num5):
        return [0,0,0,0,1,0,0,0,0]
    elif np.all(val == num6):
        return [0,0,0,0,0,1,0,0,0]
    elif np.all(val == num7):
        return [0,0,0,0,0,0,1,0,0]
    elif np.all(val == num8):
        return [0,0,0,0,0,0,0,1,0]
    elif np.all(val == num9):
        return [0,0,0,0,0,0,0,0,1]

    
def backprop(n = 1):
    """Performs the backpropagation algorithm over N epochs, returns error function"""
    global E
    E = []
    global w1
    global w2
    for i in np.arange(n):
        e = 0.0

        global p
        global o
        global e
        for p in patterns:
            o = calculate_response(p)
            e += error(p, o)
            
            global do
            global dh
            global dw2
            global dw1
            # Error in output layer
            o_error = target(p) - o
            do = o_error * logistic(o, deriv = True)
            
            # error in hidden layer
            h_error = np.dot(do, w2.T) 
            dh = h_error * logistic(h, deriv = True)
            
            #had to replicate h,x arrays to get dot to work?
            dw2 = np.dot(np.repeat(h[:, np.newaxis], 9, axis=1), do.T)             
            dw1 = np.dot(np.repeat(x[:, np.newaxis], 5, axis=1), dh)

            
            #replicating again?
            w2 += eta * np.repeat(dw2[:, np.newaxis], 9, axis=1)
            w1 += eta * np.repeat(dw1[:, np.newaxis], 5, axis=1)
        
        E.append(e)  # Error at epoch i 
    return E  # Returns the list of error by epoch
            

# Plot the error function by epoch
backprop(10000)
plt.plot(E, "r-")
plt.xlabel("Training epoch")
plt.ylabel("Error")
plt.title("XOR classification error by epoch")
plt.show()

# Plot the responses to the XOR patterns
y_end = [calculate_response(p) for p in patterns]
fig, ax = plt.subplots()
ax.axis([-0.5, 3.5, 0, 1])
ax.set_xticks(np.arange(10))
#ax.set_xticklabels(["(%s,%s)" % tuple(p) for p in patterns])
ax.set_ylabel("Activation")
ax.set_xlabel("Patterns")
ax.bar(np.arange(9) - 0.25, y_end[1], 0.5, color='black')
ax.set_title("Responses to XOR patterns")
plt.show()

