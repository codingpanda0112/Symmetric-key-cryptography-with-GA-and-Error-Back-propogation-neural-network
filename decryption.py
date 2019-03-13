from math import exp
from random import seed
from random import random
 
# Initialize a weights_and_bias
def initialize(no_of_inputs, no_of_hidden, no_of_outputs):
	weights_and_bias = list()
	hidden_layer = [{'weights':[random() for i in range(no_of_inputs + 1)]} for i in range(no_of_hidden)]
	weights_and_bias.append(hidden_layer)
	output_layer = [{'weights':[random() for i in range(no_of_hidden + 1)]} for i in range(no_of_outputs)]
	weights_and_bias.append(output_layer)
	return weights_and_bias
 
# Calculate perceptron activation for an input
def activation_function(weights, inputs):
	activation = weights[-1]
	for i in range(len(weights)-1):
		activation += weights[i] * inputs[i]
	return activation
 
# sigmoid_function perceptron activation
def sigmoid_function(activation):
	return 1.0 / (1.0 + exp(-activation))
 
# Forward propagate input to a weights_and_bias output
def forward_propagation(weights_and_bias, row):
	inputs = row
	for layer in weights_and_bias:
		new_inputs = []
		for perceptron in layer:
			activation = activation_function(perceptron['weights'], inputs)
			perceptron['output'] = sigmoid_function(activation)
			new_inputs.append(perceptron['output'])
		inputs = new_inputs
	return inputs
 
# Calculate the derivative of an perceptron output
def sigmoid_function_derivative(output):
	return output * (1.0 - output)
 
# Backpropagate error and store in perceptrons
def error_propagation(weights_and_bias, expected):
	for i in reversed(range(len(weights_and_bias))):
		layer = weights_and_bias[i]
		errors = list()
		if i != len(weights_and_bias)-1:
			for j in range(len(layer)):
				error = 0.0
				for perceptron in weights_and_bias[i + 1]:
					error += (perceptron['weights'][j] * perceptron['diff'])
				errors.append(error)
		else:
			for j in range(len(layer)):
				perceptron = layer[j]
				errors.append(expected[j] - perceptron['output'])
		for j in range(len(layer)):
			perceptron = layer[j]
			perceptron['diff'] = errors[j] * sigmoid_function_derivative(perceptron['output'])
 
# Update weights_and_bias weights with error
def update_weights(weights_and_bias, row, l_rate):
	for i in range(len(weights_and_bias)):
		inputs = row[:-1]
		if i != 0:
			inputs = [perceptron['output'] for perceptron in weights_and_bias[i - 1]]
		for perceptron in weights_and_bias[i]:
			for j in range(len(inputs)):
				perceptron['weights'][j] += l_rate * perceptron['diff'] * inputs[j]
			perceptron['weights'][-1] += l_rate * perceptron['diff']
 
# Train a weights_and_bias for a fixed number of epochs
def train_weights_and_bias(weights_and_bias, train, l_rate, n_epoch, no_of_outputs,target):
	for epoch in range(n_epoch):
		sum_error = 0
		j=0
		for row in train:
			outputs = forward_propagation(weights_and_bias, row)
			expected = [0 for i in range(no_of_outputs)]
			expected[target[j][-1]] = 1
			#print(target[j][0])
			#print(row[-1])
			j+=1
			sum_error += sum([(expected[i]-outputs[i])**2 for i in range(len(expected))])
			error_propagation(weights_and_bias, expected)
			update_weights(weights_and_bias, row, l_rate)
			
		print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))
 
# Make a prediction with a weights_and_bias
def predict(weights_and_bias, row):
	outputs = forward_propagation(weights_and_bias, row)
	print outputs
	return outputs.index(max(outputs))


# Test training backprop algorithm
seed(1)

dataset = []
dataset_target = []
binary = ['00101000', '00111011', '00010001', '01100010', '00000001', '11110000', '00010000', '01100000', '00010011', '00111011', '00010011', '00110010', '00010011', '00000001', '00010011', '00100000', '00110001', '00010011', '00011010', '00100001', '00010010', '00110011', '00100101', '00101000', '00000011', '00010001', '00100101', '00100000', '00000010', '00110011', '11010011', '00110000', '00110011', '00010011', '00100110', '00110000', '00000011', '01101001', '00011011', '01010000', '00000001', '00000111', '01111011', '01100000', '00010001', '00101011', '00110001', '00111001', '00100001', '00100011', '01110000', '00000111', '00010001', '00110011', '00110010', '00100000', '00010000', '00011011', '01000110', '00000010', '00010011', '00010011', '01000000', '00110010', '00100011', '10111010', '00110100', '00110010', '01000000', '00000001', '00110010', '01100011', '00000011', '10110001', '00110010', '00101011', '00011000', '00110011', '00101110', '00000000', '00111001', '00001001', '00000110', '00100000', '00010001', '01101111', '00010010', '01100011', '01010010', '00010001', '00100011', '00011010', '00111000', '00010001', '00110000']
target = ['00110000', '00111000', '00110100', '00100000', '00110001', '00110000', '00110100', '00100000', '00110001', '00110000', '00110101', '00100000', '00110001', '00110001', '00110101', '00100000', '00110000', '00110011', '00110010', '00100000', '00110001', '00110000', '00110101', '00100000', '00110001', '00110001', '00110101', '00100000', '00110000', '00110011', '00110010', '00100000', '00110001', '00110000', '00110101', '00100000', '00110001', '00110000', '00111001', '00100000', '00110001', '00110001', '00110010', '00100000', '00110001', '00110001', '00110001', '00100000', '00110001', '00110001', '00110100', '00100000', '00110001', '00110001', '00110110', '00100000', '00110000', '00111001', '00110111', '00100000', '00110001', '00110001', '00110000', '00100000', '00110001', '00110001', '00110110', '00100000', '00110000', '00110011', '00110010', '00100000', '00110001', '00110000', '00110000', '00100000', '00110000', '00111001', '00110111', '00100000', '00110001', '00110001', '00110110', '00100000', '00110000', '00111001', '00110111', '00100000', '00110000', '00110001', '00110011', '00100000', '00110000', '00110001', '00110000']
for strings in binary:
	strings = list(strings)
	for bit in strings:
		bit = int(bit)
		number=[]
		number.append(bit)
		dataset.append(number)
print dataset
for strings in target:
	strings = list(strings)
	for bit in strings:
		bit = int(bit)
		number=[]
		number.append(bit)
		dataset_target.append(number)

no_of_inputs = 1#len(dataset[0]) - 1
#no_of_outputs = len(set([row[-1] for row in dataset]))
no_of_outputs = 2
weights_and_bias = initialize(no_of_inputs, 2, no_of_outputs)
train_weights_and_bias(weights_and_bias, dataset, 0.5, 20, no_of_outputs,dataset_target)
for layer in weights_and_bias:
	print(layer)

count = 0
i = 0
for row in dataset:
	prediction = predict(weights_and_bias, row)
	if dataset_target[i][0] == prediction:
		count+=1
	print('Expected=%d, Got=%d' % (dataset_target[i][0], prediction))
	i+=1

accuracy = count//len(dataset)
#print "accuracy=", accuracy
