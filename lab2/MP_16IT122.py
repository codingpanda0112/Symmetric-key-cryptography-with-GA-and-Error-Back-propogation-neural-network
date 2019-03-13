import csv
from math import exp
from random import random

# Initialize a network
def initialize_network(n_inputs, n_hidden, n_outputs):
	network = list()
	hidden_layer = [{'weights':[random() for i in range(n_inputs + 1)]} for i in range(n_hidden)]
	#print(hidden_layer)
	network.append(hidden_layer)
	output_layer = [{'weights':[random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
	#print(output_layer)
	network.append(output_layer)
	#print(network)

	return network

def activate(weights, inputs):
	activation = weights[-1]
	#print(activation)
	count=0
	for i in range(len(weights)-1):
		activation += weights[i] * inputs[i]

	#print(activation)
	return activation

def transfer(activation):
	return 1.0 / (1.0 + exp(-activation))

def forward_propagate(network, row):
	inputs = row

	for layer in network:
		new_inputs = []
		for neuron in layer:
			activation = activate(neuron['weights'], inputs)
			neuron['output'] = transfer(activation)
			new_inputs.append(neuron['output'])
			
		inputs = new_inputs
		#print(inputs)
	return new_inputs     #outout given by the output layer

def transfer_derivative(output):
	return output * (1.0 - output)

def backward_propagate_error(network, expected):
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
				#print(neuron)
				errors.append(expected[j] - neuron['output'])
		for j in range(len(layer)):
			neuron = layer[j]
			neuron['delta'] = errors[j] * transfer_derivative(neuron['output'])

def update_weights(network, row, l_rate):
	for i in range(len(network)):
		inputs = row[:-1]
		if i != 0:
			inputs = [neuron['output'] for neuron in network[i - 1]]
		for neuron in network[i]:
			for j in range(len(inputs)):
				neuron['weights'][j] += l_rate * neuron['delta'] * inputs[j]
			neuron['weights'][-1] += l_rate * neuron['delta']


def train_network(network,train_set,n_outputs,l_rate):
	sum_error=0
	for row in train_set:
			outputs = forward_propagate(network, row)
			#print(outputs)
			expected = [0 for i in range(n_outputs)]
			#print(row[-1])
			expected[row[-1]] = 1
			#print(expected)
			sum_error += sum([(expected[i]-outputs[i])**2 for i in range(len(expected))])
			backward_propagate_error(network, expected)
			update_weights(network, row, l_rate)
	print(sum_error)

def str_to_float(rows,pos):
	for row in rows:
		for index,item in enumerate(row):
			if index!=pos:
				row[index]=float(item)
		#print(row)
	return rows

def expected(rows,pos):
	class_values=[]
	#class_values = set()
	hash_map={}
	actual=[None for i in range(len(rows))]
	for row in rows:
		if row[pos] not in class_values:
			class_values.append(row[pos])
		#print(row)
	#print(class_values)
	count=0
	for items in class_values:
		hash_map[items]=count
		count+=1
	#print(hash_map)
	for i in range(len(rows)):
		rows[i][pos] = hash_map[rows[i][pos]]
	#for row in rows:
	#print(row)
	return rows

def readfile():
	filename = "IRIS.csv"
	rows = []
	with open(filename,"r") as csvfile:
		csvreader = csv.reader(csvfile)
		field= next(csvreader)
		#length_col = len(field)
		#print(i)
		#getting the column  number of the field column
		pos=field.index("class" or "Class")
		#print(pos)
		#making the excel sheet into a list
		#length_row = 0
		for row in csvreader:
			#length_row+=1
			rows.append(row)

	
	n_inputs = len(rows[0])-1
	n_outputs = len(set([row[-1] for row in rows]))
	#print(n_inputs,n_outputs)

	rows=expected(rows,n_inputs)
	#print(rows)
	rows=str_to_float(rows,n_inputs)
	#print(rows)
	network = initialize_network(n_inputs, 2, n_outputs)

	#for layer in network:
	#	print(layer)


	#print(length_row)
	#print(rows)
	#Expected value for the class column
	#-------rows=expected(rows,pos)
	#print(rows)
	#convert from string to float
	#-------rows=str_to_float(rows,pos)
	#print(rows)
	fold  = 9*len(rows)//10
	train_set = rows[:fold]
	test_set = rows[fold:]

	l_rate=0.1
	train_network(network,train_set,n_outputs,l_rate)
	#print(test_set)
	#print(len(test_set))
	#-----------z = threshold(rows,length_row,length_col,pos)
	#print(threshold(rows,length_row,length_col,pos))
	#predict(rows,length_row,length_col,pos,z)
	#---------weights=[1/((length_col-1)+1) for i in range(length_col-1)]
	#---------weights=predict(train_set,length_row,length_col,pos,z,weights)
	#----------accuracy = test_model(test_set,pos,len(test_set),z,weights)
	#------print("Accuracy=",accuracy)


def main():
	readfile()

if __name__ == '__main__':
	main()
