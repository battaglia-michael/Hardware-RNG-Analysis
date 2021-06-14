import numpy as np
import matplotlib.pyplot as plt
 
V, Verr, I, Ierr = np.loadtxt("chua.txt", comments=';', unpack=True)
 
plt.errorbar(V, I, xerr=Verr, yerr=Ierr)
plt.xlabel("Voltage (V)")
plt.ylabel("Current (mA)")
plt.title("Chua's Diode")
plt.show()
