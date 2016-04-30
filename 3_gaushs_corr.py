## Tutorial1 Question3:
## Using the results of part 1 and part 2, write a routine to take the correlation,
## function of a Gaussian (shifted by an arbitrary amount) with itself. 
#
from numpy import exp, real, pi, complex, linspace, arange,conj
from numpy.fft import fft,ifft
from matplotlib import pyplot as plt
def convl(gaus,hflen):
    gaus_ft = fft(gaus)
    return real(ifft(gaus_ft*hflen))

x = linspace(-10,10,200)
sig = 0.5; N = len(x); dx = 50; k = arange(N);J = complex(0,1)
gaus = exp(-0.5*x**2/sig**2)
hflen = exp(2*pi*J*k*dx/N)
h = convl(gaus,hflen)
plt.plot(x,h,'b')
h1 = convl(gaus,hflen)
def corrl(h,h1):
    ft = fft(h)
    cj = conj(fft(h1))
    return ifft(ft*cj)
H = corrl(h,h1)
H1 = real(H)
plt.plot(x,H1,'r')
plt.grid(True)
plt.title('Correlation of Gaussion shifted with itself')
plt.show()

# How does the correlation function depend on the shift? Does this surprise you?
print 'The correlation is invariant by the shifft.'
