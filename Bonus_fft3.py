#    Tutorial3 Bonus:
##  You have a sample code that calculates an FFT of an array whose length is 
##  a power of 2. Using that routine as a guideline, write an FFT routine that 
##  works on an array whose length is a power of 3 (e.g. 9, 27, 81). Verify that 
##  it gives the same answer as numpy.fft.fft 
#######################
# I divide the array in to 3 equal parts I, II and III
import numpy as np
def FFT(x):
    x = np.asarray(x, dtype=float)
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    m = np.arange(N/3)
    if N % 3 > 0:
        raise ValueError("size of x must be a power of 3")
    else:
        expo = np.exp(-2j*np.pi*k*m/(N/3))
        x1  = (x[::3])
        X_I = np.dot(expo,x1)
        x2  = (x[1::3])
        X_II = np.dot(expo,x2)
        x3  = (x[2::3])
        X_III = np.dot(expo,x3)
        #X_I = FFT(x[::3])
        #X_II = FFT(x[1::3])
        #X_III = FFT(x[2::3])
        factor = np.exp(-2j * np.pi * k/ N)
        return X_I + factor*X_II + (factor**2)*X_III
        #return np.concatenate([X_I + factor[N/3:2*(N/3)] * X_II  + factor[2*(N/3):]**2*X_III])
                              #X_I + factor[N/3:2*(N/3)]*X_II +factor[N/3:2*(N/3)]**2*(X_III),
                              #X_I + factor[2*(N/3):] * X_II + factor[2*(N/3):]**2*X_III])

x = np.random.random(729) 

#print np.allclose(FFT(x), np.fft.fft(x))
