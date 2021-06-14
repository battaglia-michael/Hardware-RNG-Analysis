from __future__ import division
import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

def power_spectrum(t,y):
    N = len(t)                       # this is the number of acquired data samples
    sampling_rate = 1/(t[1]-t[0])    # this is Delta f
    # FFT refers to the Fast Fourier Transform,
    # an efficient algorithm to calculate the fourier components Y(f)
    Y = np.fft.fft(y)/np.sqrt(N) 
    f = np.fft.fftfreq(N,1/sampling_rate)
    
    # Y has fourier components at both positive & negative frequencies
    # we will pick out only the positive frequencies, and use them to define W_y(f)
    
    return f[1:int(N/2)],(2 * np.abs(Y)**2/sampling_rate)[1:int(N/2)]


# uncomment this line to input a waveform from a file
t,y = np.loadtxt("trace1.txt",unpack=True)

# test data to demonstrate a power spectrum plot
t = np.arange(0,10,0.01)
y = 6 + np.sin(2*pi*6*t) + np.cos(2*pi*10*t)

f,W = power_spectrum(t,y)

## Log-log plot of power spectrum

fig = plt.figure()
ax = fig.add_subplot(111)
ax.loglog(f,W)
ax.set_xlabel("frequency [Hz]")
ax.set_ylabel("power spectral density [V$^2$/Hz]")
plt.show()
