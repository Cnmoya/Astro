#UTF-8
from astropy.io import fits
import matplotlib.pyplot as plt
from overscan import plot_os
import sys
print(sys.argv)
imagen=fits.open(sys.argv[1])[0]
data,header= imagen.data, imagen.header
plot_os(data)
plt.show()
