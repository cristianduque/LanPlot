from scipy.fftpack import fft
import matplotlib.pyplot as plt
from numpy import cos,linspace,pi,abs,sin,heaviside,exp


class FourierTransform(object):
   def __init__(self, equation, number_samples):
      self.equation = equation
      self.number_samples = number_samples

   def compute(self):
      N = self.number_samples # Number of samplepoints
      T = 1 / N    # sample spacing
      t = linspace(0.0, N * T, N)  #time domain

      transform_equation = eval(self.equation)

      fourier_equation = fft(transform_equation)  # fft computing and normalization

      frequency_domain = linspace(0.0, 1.0 / (2.0 * T), N // 2)

      plt.title("Fourier Transform Graph")
      plt.xlabel("Frequency")
      plt.ylabel("Fourier Equation")
      plt.plot(frequency_domain, 2.0 / N * (abs(fourier_equation[0:N // 2])))  # one side frequency range and plotting spectrum
      plt.grid()
      plt.show()

   def computefft(self):
      N = self.number_samples
      T = 1 / N
      t = linspace(0.0, N * T, N)
      transform_equation = eval(self.equation)
      fourier_equation = fft(transform_equation)
      return fourier_equation

def plotfft(equation):
    N = 1000
    T = 1 / N
    frequency_domain = linspace(0.0, 1.0 / (2.0 * T), N // 2)
    plt.title("Fourier Transform Graph")
    plt.xlabel("Frequency")
    plt.ylabel("Fourier Equation")
    plt.plot(frequency_domain, 2.0 / N * (abs(equation[0:N // 2])))
    plt.grid()
    plt.show()

