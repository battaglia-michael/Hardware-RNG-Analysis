# Hardware-RNG-Analysis
Constructed a hardware random number generator (RNG) based on the Chua differential equations.

The main results with visualizations can be found in the writeup *ChuaReport.pdf*.
Group collaboration with Chris Ni.

Measured amount of randomness and constrasted with Python's Mersenne Twister through the use of a Monte Carlo method for approximating pi.
As well, the *DoubleScroll.mp4/jpg* files show a cool oscilloscope visualization of randomness, and *MonteCarloOutput.jpg* shows the pi approximation.

While portions of the code cannot be run without collecting data from an oscilloscope, there is sample collected Voltage data in collectOscilloscopeV.
Coded using Python 2.7, necessary libraries are PyVISA, numpy, scipy, and matplotlib.

Note that *ChuaHRNG.ino* is for communication with a RaspberryPi to sample outputs from the circuit.
