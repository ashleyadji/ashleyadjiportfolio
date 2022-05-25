import math

# 2 inputs, 1 hidden with 2 nodes, single output

class Neuron:
  def __init__(self,weight1,weight2,activationfunct):
    self.weight1 = weight1
    self.weight2 = weight2
    self.activationfunct = activationfunct
    
  def run(self,input1,input2,bias):
    return self.activationfunct(input1*self.weight1 + input2*self.weight2 + bias)
  
def sigmoid(x):
  return 1/(1 + math.pow(math.e,-x))

def relu(x):
  if x > 0:
    return x
  if x <= 0:
    return 0

x1 = 0
x2 = 1
bias = 1

h1 = Neuron(1,2,sigmoid)
h2 = Neuron(3,1,sigmoid)
output = Neuron(3,5,relu)

h1output = h1.run(x1,x2,bias)
h2output = h2.run(x1,x2,bias)
outputoutput = output.run(h1output,h2output,bias)

print(h1output)
print(h2output)
print(outputoutput)
