import numpy as np
import matplotlib.pyplot as plt
from numpy import  pi

Fs=44100                # Sampling Frequency in Hz
Ts=1/Fs                 # Sampling Interval in Hz
duration = 100          # Duration of signal in ms
t=np.arange(0, duration/1000,Ts)

f=100                   # Frequency of signal
A=1                     # Amplitude

x_t = A*np.sin(2*pi*f*t) # x(t) = A sin(2 pi f t)

# PLotting
plt.plot(t*1000,x_t)
plt.xlabel("time in ms"); plt.ylabel("Amplitude")
plt.show()
