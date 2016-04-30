#
## Tutorial1 Question2b
## 2b)Plot the correlation function of a Gaussian with itself.
#
from numpy import pi,exp,real,conj,linspace
from numpy.fft import fft,ifft
from matplotlib import pyplot as plt
def corrl(gaus):
    ft_gaus = fft(gaus)
    cj_gaus = conj(fft(gaus))
    return ifft(ft_gaus*cj_gaus)

x = linspace(-10,10,200)
sig = 0.5
gaus = exp(-0.5*x**2/sig**2)
h = corrl(gaus)
h1 = real(h)
plt.plot(x,h1)
plt.title('Correlation of Gaussian function to itself')
plt.grid(True)
plt.show()
