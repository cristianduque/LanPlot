from scipy.fftpack import fft
import matplotlib.pyplot as plt
from numpy import cos,linspace,pi,abs

class FourierTransform(object):
   def __init__(self, equation, number_samples):
      self.equation = equation
      self.number_samples = number_samples

   def compute(self):
      N = self.number_samples
      T = 1 / N
      t = linspace(0.0, N * T, N)

      y = eval(self.equation)
      print(y)

      Xf = fft(y)

      xt = linspace(0.0, 1.0 / (2.0 * T), N // 2)

      plt.title("Fourier Transform Graph")
      plt.xlabel("Frequency")
      plt.ylabel("Fourier Equation")
      plt.plot(xt, 2.0 / N * (abs(Xf[0:N // 2])))
      plt.grid()
      plt.show()


# print(FourierTransform('cos(2*pi*50*t)', 600).compute())

