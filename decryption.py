from math import exp
from random import seed
from random import random
import csv
import numpy as np

# Initialize a network
def setnetwork(n_inputs, n_hidden, n_outputs):
	network = list()
	hidden_layer = [{'weights':[random() for i in range(n_inputs + 1)]} for i in range(n_hidden)]
	network.append(hidden_layer)
	output_layer = [{'weights':[random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
	network.append(output_layer)
	return network

# Calculate neuron activation for an input
def activate(weights, inputs):
	activation = weights[-1]
	for i in range(len(weights)-1):
		activation += weights[i] * inputs[i]
	return activation

# Transfer neuron activation
def transfer(activation):
	return 1.0 / (1.0 + exp(-activation))

# Forward propagate input to a network output
def feedforward(network, row):
	inputs = row
	for layer in network:
		new_inputs = []
		for neuron in layer:
			activation = activate(neuron['weights'], inputs)
			neuron['output'] = transfer(activation)
			new_inputs.append(neuron['output'])
		inputs = new_inputs
	return inputs

# Calculate the derivative of an neuron output
def derivative(output):
	return output * (1.0 - output)

# Backpropagate error and store in neurons
def backpropogation(network, expected):
	for i in reversed(range(len(network))):
		layer = network[i]
		errors = list()
		if i != len(network)-1:
			for j in range(len(layer)):
				error = 0.0
				for neuron in network[i + 1]:
					error += (neuron['weights'][j] * neuron['delta'])
				errors.append(error)
		else:
			for j in range(len(layer)):
				neuron = layer[j]
				errors.append(expected[j] - neuron['output'])
		for j in range(len(layer)):
			neuron = layer[j]
			neuron['delta'] = errors[j] * derivative(neuron['output'])

# Update network weights with error
def update_weights(network, row, l_rate):
	for i in range(len(network)):
		inputs = row[:-1]
		if i != 0:
			inputs = [neuron['output'] for neuron in network[i - 1]]
		for neuron in network[i]:
			for j in range(len(inputs)):
				neuron['weights'][j] += l_rate * neuron['delta'] * inputs[j]
			neuron['weights'][-1] += l_rate * neuron['delta']

# Train a network for a fixed number of epochs
def train_network(network, train, l_rate, n_epoch, n_outputs):
	sum_error=-1
	#strt='training.'
	print("training....data")
	for epoch in range(n_epoch):
		sum_error = 0
		for row in train:
			outputs = feedforward(network, row)
			expected = [0 for i in range(255)]
			#print(row[-1])
			expected[row[-1]] = 1
			sum_error += sum([(expected[i]-outputs[i])**2/(255*2*10) for i in range(len(expected))])
			backpropogation(network, expected)
			update_weights(network, row, l_rate)
		#print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))

		#print(strt)
		if sum_error<=0.04:
			return sum_error
	return sum_error
def loadCsv(filename):
	lines = csv.reader(open(filename, "r"))
	dataset1 = list(lines)
	dataset = []
	for item in dataset1:
		if item != []:
			dataset.append(item)
	#print(dataset)
	cipher=[]
	#print(len(dataset))
	for i in range(len(dataset)):
		dataset[i] = [int(x,2) for x in dataset[i]]
	for  i in range(len(dataset)):
		cipher.append(dataset[i][-1])

	return dataset, cipher

def predict(network, row):
	outputs = feedforward(network, row)
	return outputs.index(max(outputs))

# Test training backprop algorithm
seed(1)
filename='data12.csv'
dataset,cipher=loadCsv(filename)
#print(dataset)

n_inputs = len(dataset[0]) - 1
n_outputs = 255
#print("n out put",n_outputs)
network = setnetwork(n_inputs, 2, n_outputs)
error=train_network(network, dataset, 0.2, 5000, n_outputs)
ascii_array=[]
# first conversion of ascii value
if error<0.19:
	for item  in cipher:
		ascii_array.append(item)
else:
	print("Error")

print("first Ascii conversion[array]:")
print(ascii_array)


#second conversion to asccii value
strb=""
ascii_array1=[]
for item in ascii_array:
	character=chr(item)
	ascii_array1.append(character)
	strb=strb+character
print("First Ascii conversion:")
print(strb)
print("==========================================================")
print("Second ascii conversion:[array]")
print(ascii_array1)


decrypted_text=""
ascii_array2=[]
ascii_array2=strb.split(' ')
#print(ascii_array2)

for item in ascii_array2:
	asciivalue=int(item)
	#print(chr(asciivalue))
	decrypted_text+=chr(asciivalue)
print("final decrypted text:")
print(decrypted_text)
