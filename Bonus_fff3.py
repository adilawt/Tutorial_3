#    Tutorial3 Bonus:
##  You have a sample code that calculates an FFT of an array whose length is 
##  a power of 2. Using that routine as a guideline, write an FFT routine that 
##  works on an array whose length is a power of 3 (e.g. 9, 27, 81). Verify that 
##  it gives the same answer as numpy.fft.fft 
#######################
# I divide the array in to 3 equal parts I, II and III
import numpy
def FFT3(x):
    N=x.shape[0]
    if N==1:
        return x
    if N%3>0:
       raise ValueError("size of x numst be a power of 3")
    N3 = N/3
    fact1 = numpy.exp(-2j*numpy.pi*numpy.arange(0,N3)/N)
    fact2 = numpy.exp(-4j*numpy.pi*numpy.arange(0,N3)/N)
    
    f1 = numpy.exp(-2j*numpy.pi/3)
    f2 = numpy.exp(-4j*numpy.pi/3)
    
    aft = FFT3(x[0::3])
    bft = FFT3(x[1::3])*fact1
    cft = FFT3(x[2::3])*fact2

    ft1 = aft+bft+cft
    ft2 = aft+bft*f1+cft*f2
    ft3 = aft+bft*f2+cft*f1
    return numpy.concatenate((ft1,ft2,ft3))


x = numpy.random.randn(729)
print 'the size of x, a number power of 3 is:', len(x)
print 'comparing FFT3 and numpy.fft.fft results:', numpy.allclose(FFT3(x),numpy.fft.fft(x))
print '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
print '+---------------------------------------------------------+'
print '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
x1 = numpy.random.randn(100)
print 'the size of x1, a number different from pwoer 3 is:', len(x1)
print numpy.allclose(FFT3(x1),numpy.fft.fft(x1))
