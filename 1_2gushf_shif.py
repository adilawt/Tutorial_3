## Tutorial1 Question1.b
## b)Plot a gaussian that started in the centre of the array shifted by half the array length. 
##
#
import numpy as np
from matplotlib import pyplot as plt
def convl(f,hflen):
    ft = np.fft.fft(f)
    return np.real(np.fft.ifft(ft*hflen))

x = np.linspace(-10,10,200)
sig = 0.5
f= np.exp(-0.5*x**2/sig**2)
N = len(x)
k = np.arange(N)
J = np.complex(0,1)
dx = len(x)/2 # this shift value which is half of the length of the array
hflen = np.exp(-2*np.pi*J*k*dx/N)
h = convl(f,hflen)

plt.plot(x,f,'b')
plt.plot(x,h,'r')
plt.grid(True)
plt.title('Gaussian half length shift')
plt.show()
