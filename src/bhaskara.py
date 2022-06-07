import sys
from math import sqrt
from numpy import arange
from matplotlib import pyplot as plt

class Bhaskara:
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c
    self._x1 = None
    self._x2 = None
    self._delta = None

  def calculate(self, a = None, b = None, c = None):
    if a is None: a = self.a
    if b is None: b = self.b
    if c is None: c = self.c

    self._delta = self.__calculateDelta(a, b, c)
    self._x1, self._x2 = self.__calculateRoots(a, b, self._delta)

    print(f'Delta: {self._delta}\n(X1: {self._x1}, X2: {self._x2})')

    if self._x1 == self._x2: return self._x1
    else: return self._x1, self._x2

  @staticmethod
  def __calculateDelta(a, b, c):
    return (b ** 2) - 4 * a * c

  @staticmethod
  def __calculateRoots(a, b, delta):
    if delta < 0:
      raise Exception('Impossível continuar.. Não existe raíz de número negativo.')
    
    firstRoot = ((b * -1) + sqrt(delta)) / (2 * a)
    secondRoot = ((b * -1) - sqrt(delta)) / (2 * a)

    return firstRoot, secondRoot
  
  def plot(self):
    xAxis = []
    yAxis = []
    zero = []

    variation = abs(self._x1 - self._x2)
    if variation < 3: variation = 3

    for x in arange(self._x1 - variation, self._x2 + variation, variation / 100):
      y = self.a * (x ** 2) + self.b * x + self.c
      xAxis.append(x)
      yAxis.append(y)
      zero.append(0.0)
    
    plt.figure('Bhaskara plot', figsize=(10,7))
    plt.title(f'$f(x) = {self.a:.0f}x^2 {self.b:+.0f}x {self.c:+.0f}$', fontsize=14)
    plt.xlabel(f'x \n $\Delta = {self._delta}$')
    plt.ylabel('y', rotation=0)

    offsetX = 0.06
    offsetY = 0.2

    plt.annotate(self._x1, [self._x1 + offsetX, 0 + offsetY], fontsize=10)
    plt.scatter(self._x1, 0, 35, color='mediumpurple', label='X1')

    if self._x1 != self._x2:
      plt.annotate(self._x2, [self._x2 + offsetX, 0 + offsetY], fontsize=10)
      plt.scatter(self._x2, 0, 35, color='darksalmon', label='X2')

    plt.plot(xAxis, yAxis, color="slateblue")
    plt.plot(xAxis, zero, color="dimgray")

    plt.legend()
    plt.show()


def main():
  args = sys.argv[1:]

  if len(args) == 3:
    a = float(args[0])
    b = float(args[1])
    c = float(args[2])
  else:
    a, b, c = getTerms()

  bhaskara = Bhaskara(a, b, c)
  bhaskara.calculate()
  bhaskara.plot()

def getTerms():
  a = float(input('Digite A: '))
  b = float(input('Digite B: '))
  c = float(input('Digite C: '))
  return a, b, c

if __name__ == "__main__":
  main()
