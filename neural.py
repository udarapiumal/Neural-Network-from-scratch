import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

class neuron:
    def __init__(self,weights,bias):
        self.weights=weights
        self.bias=bias
        
    def feedforward(self,inputs):
        total=np.dot(inputs,self.weights) + self.bias
        return sigmoid(total)
    
    
weights=np.array([0,1])
bias=0
inputs=np.array([2,3])

n1=neuron(weights,bias)
n2=neuron(weights,bias)
o=neuron(weights,bias)

output1=n1.feedforward(inputs)
output2=n2.feedforward(inputs)

inputs2=np.array([output1,output2])
output=o.feedforward(inputs2)

print(output)