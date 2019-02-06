from Matrix import *
import math

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

def dsigmoid(y):
  return y * (1 - y)

def sech2(x):
  return 2 / (math.exp(x) + math.exp(-x))

class NeuralNetwork():
  def __init__(self, input_nodes, hidden_nodes, output_nodes):
    self.input_nodes = input_nodes
    self.hidden_nodes = hidden_nodes
    self.output_nodes = output_nodes

    self.weights_ih = Matrix(self.hidden_nodes, self.input_nodes)
    self.weights_ho = Matrix(self.output_nodes, self.hidden_nodes)
    self.weights_ih.randomize(0,1)
    self.weights_ho.randomize(0,1)

    self.bias_h = Matrix(self.hidden_nodes, 1)
    self.bias_o = Matrix(self.output_nodes, 1)
    self.bias_h.randomize(0,1)
    self.bias_o.randomize(0,1)

    self.learning_rate = 0.0001

  def guess(self, inputs):
    #generate hidden nodes
    hidden = Matrix.matrix_multiply(self.weights_ih, inputs)
    hidden = Matrix.add(hidden, self.bias_h)
    #apply activation function
    hidden = Matrix.map_function(hidden, math.tanh)

    #generate output nodes
    outputs = Matrix.matrix_multiply(self.weights_ho, hidden)
    outputs = Matrix.add(outputs, self.bias_o)
    #apply activation function
    outputs = Matrix.map_function(outputs, math.tanh)

    outputs.print()

  def train(self, inputs, targets):
    #feed forward process
    hidden = Matrix.matrix_multiply(self.weights_ih, inputs)
    hidden = Matrix.add(hidden, self.bias_h)
    hidden = Matrix.map_function(hidden, math.tanh)
    outputs = Matrix.matrix_multiply(self.weights_ho, hidden)
    outputs = Matrix.add(outputs, self.bias_o)
    outputs = Matrix.map_function(outputs, math.tanh)
    #outputs.print()

    #calculate error
    #error = outputs - targets
    output_errors = Matrix.subtract(targets, outputs)

    

    #calculate gradients
    gradients = Matrix.map_function(outputs, sech2)
    gradients = Matrix.element_multiply(outputs, output_errors)
    gradients = Matrix.scalar_multiply(outputs, self.learning_rate)

    

    #calculate hidden to output deltas
    hidden_t = Matrix.transpose(hidden)
    weights_ho_deltas = Matrix.matrix_multiply(gradients, hidden_t)

    #adjust weights by deltas
    self.weights_ho = Matrix.add(self.weights_ho, weights_ho_deltas)
    #adjust bias by its deltas aka the gradients
    self.bias_o = Matrix.add(self.bias_o, gradients)

    #calculate hidden layer errors
    weights_ho_t = Matrix.transpose(self.weights_ho)
    hidden_errors = Matrix.matrix_multiply(weights_ho_t, output_errors)

    #calculate hidden gradient
    hidden_gradient = Matrix.map_function(hidden, sech2)
    hidden_gradient = Matrix.element_multiply(hidden_gradient, hidden_errors)
    hidden_gradient = Matrix.scalar_multiply(hidden_gradient, self.learning_rate)

    #calculate input to hidden deltas
    inputs_t = Matrix.transpose(inputs)
    weights_ih_deltas = Matrix.matrix_multiply(hidden_gradient, inputs_t)

    self.weights_ih = Matrix.add(self.weights_ih, weights_ih_deltas)
    #adjust bias by its deltas aka the gradients
    self.bias_h = Matrix.add(self.bias_h, hidden_gradient)
