from PIL import Image

class Picture():
  def __init__(self, photo):
    self.img = Image.open(photo)
    self.pic = self.img.load()
    side = 15
    size = side ** 2
    self.matrix = [[0 for y in range(1)] for x in range(size)]
    counter = 0
    total = 0
    for x in range(side):
      for y in range(side):
        self.matrix[counter] = [int('%02x%02x%02x' % self.pic[x,y], 16)]
        if self.matrix[counter] > [0]:
            self.matrix[counter] = [1]
        total += self.matrix[counter][0]
        counter += 1
    mean = total / size
    numerator = 0
    for x in range(len(self.matrix)):
      for y in range(len(self.matrix[0])):
        numerator += (self.matrix[x][y] - mean) ** 2
    variance = numerator / size
    for x in range(len(self.matrix)):
      for y in range(len(self.matrix[0])):
        self.matrix[x][y] = (self.matrix[x][y] - mean) / variance
    #print(self.matrix)

    
