import numpy as np
import matplotlib.pyplot as plt
 
f, Vi, Vierr, Vo, Voerr = np.loadtxt("antoniou.txt", comments=';', unpack=True)

H = Vo/Vi
Herr = H*np.sqrt(np.square(Vierr/Vi)+np.square(Voerr/Vo))

plt.errorbar(f, H, yerr=Herr)
plt.plot(f, [1.0/np.sqrt(2)]*len(f))
plt.xlabel("H")
plt.ylabel("freq (Hz)")
plt.title("Antoniou's Inductor")
plt.ylim(10**-2,10**0.2)
plt.xscale('log')
plt.yscale('log')
plt.show()
