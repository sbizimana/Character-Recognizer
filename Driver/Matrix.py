import random

class Matrix():
  def __init__(self, rows=None, cols=None, matrix=None):
    if matrix == None:
      self.rows = rows
      self.cols = cols
      self.mat = [[0 for y in range(self.cols)] for x in range(self.rows)]
    else:
      matrix_length = len(matrix[0])
      proceed = True
      for x in matrix:
        if len(x) != matrix_length:
          print("The matrix must be a square matrix.")
          proceed = False
          break
      if proceed:
        self.mat = matrix
        self.rows = len(self.mat)
        self.cols = len(self.mat[0])
    
  @classmethod
  def from_matrix(cls, matrix):
    return cls(None, None, matrix)

  def randomize(self, mean, stdev):
    self.mat = [[random.gauss(mean, stdev) for y in range(self.cols)] for x in range(self.rows)]

  def print(self):
    for line in self.mat:
      print(' '.join(map(str, line)))
    print("\n")

  def add(matrix_a, matrix_b):
    if matrix_a.rows != matrix_b.rows or matrix_a.cols != matrix_b.cols:
      print("You can only add matricies of the same size.")
      return
    else:
      matrix_c = Matrix(matrix_a.rows, matrix_b.cols)
      for x in range(matrix_c.rows):
        for y in range(matrix_c.cols):
          matrix_c.mat[x][y] = matrix_a.mat[x][y] + matrix_b.mat[x][y]
      return matrix_c
  
  def subtract(matrix_a, matrix_b):
    if matrix_a.rows != matrix_b.rows or matrix_a.cols != matrix_b.cols:
      print("You can only subtract matricies of the same size.")
      return
    else:
      matrix_c = Matrix(matrix_a.rows, matrix_b.cols)
      for x in range(matrix_c.rows):
        for y in range(matrix_c.cols):
          matrix_c.mat[x][y] = matrix_a.mat[x][y] - matrix_b.mat[x][y]
      return matrix_c

  def element_multiply(matrix_a, matrix_b):
    if matrix_a.rows != matrix_b.rows or matrix_a.cols != matrix_b.cols:
      print("You can only element-wise multiply matricies of the same size.")
      return
    else:
      matrix_c = Matrix(matrix_a.rows, matrix_b.cols)
      for x in range(matrix_c.rows):
        for y in range(matrix_c.cols):
          matrix_c.mat[x][y] = matrix_a.mat[x][y] * matrix_b.mat[x][y]
      return matrix_c

  def scalar_multiply(matrix_a, num):
    for x in range(matrix_a.rows):
      for y in range(matrix_a.cols):
        matrix_a.mat[x][y] *= num
    return matrix_a
        
  def scalar_divide(matrix_a, num):
    for x in range(matrix_a.rows):
      for y in range(matrix_a.cols):
        matrix_a.mat[x][y] /= num
    return matrix_a

  def transpose(matrix_a):
    matrix_b = Matrix(matrix_a.cols, matrix_a.rows)
    for x in range(matrix_b.rows):
      for y in range(matrix_b.cols):
        matrix_b.mat[x][y] = matrix_a.mat[y][x]
    return matrix_b

  def matrix_multiply(matrix_a, matrix_b):
    if matrix_a.cols != matrix_b.rows:
      print("The number of columns in the first matrix must equal the number of rows in the second matrix.")
      return
    else:
      matrix_c = Matrix(matrix_a.rows, matrix_b.cols)
      for x in range(matrix_c.rows):
        for y in range(matrix_c.cols):
          for i in range(matrix_b.rows):
            matrix_c.mat[x][y] += matrix_a.mat[x][i] * matrix_b.mat[i][y]
      return matrix_c

  def map_function(matrix_a, func):
    matrix_b = Matrix(matrix_a.rows, matrix_a.cols)
    for x in range(matrix_a.rows):
      for y in range(matrix_a.cols):
        matrix_b.mat[x][y] = func(matrix_a.mat[x][y])
    return matrix_b