from Matrix import *
from Picture import *
from NeuralNetwork import *
import random

'''picture = Picture("Letters/A/A07.png")
pix = Matrix.from_matrix(picture.matrix)
pix.print()'''

nn = NeuralNetwork(225,10,2)

training_data = [
[Picture("Letters/A/A01.png").matrix, [[1],[0]]],
[Picture("Letters/A/A02.png").matrix, [[1],[0]]],
[Picture("Letters/A/A03.png").matrix, [[1],[0]]],
#[Picture("Letters/A/A04.png").matrix, [[1],[0]]],
#[Picture("Letters/A/A05.png").matrix, [[1],[0]]],
#[Picture("Letters/B/B01.png").matrix, [[0],[1]]],
#[Picture("Letters/B/B02.png").matrix, [[0],[1]]],
[Picture("Letters/B/B03.png").matrix, [[0],[1]]],
[Picture("Letters/B/B04.png").matrix, [[0],[1]]],
[Picture("Letters/B/B05.png").matrix, [[0],[1]]]]



nn.guess(Matrix.from_matrix(Picture("Letters/A/A06.png").matrix))
nn.guess(Matrix.from_matrix(Picture("Letters/B/B06.png").matrix))

for x in range(10000):
  print(x)
  random.shuffle(training_data)
  for data in training_data:
    nn.train(Matrix.from_matrix(data[0]), Matrix.from_matrix(data[1]))

print("done training\n")

nn.guess(Matrix.from_matrix(Picture("Letters/A/A06.png").matrix))
nn.guess(Matrix.from_matrix(Picture("Letters/B/B06.png").matrix))

'''inputs = Matrix.from_matrix(picture.matrix)
targets = Matrix.from_matrix([[1],[0]])
output = nn.feed_forward(inputs)

nn.train(inputs, targets)

#output.print()'''
