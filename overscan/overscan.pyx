import numpy as np
import matplotlib.pyplot as plt
cimport numpy as np
cpdef void plot_os(data):
    cdef np.ndarray X,Y
    X=data.mean(axis=0)
    Y= np.arange(len(X))
    plt.plot(Y,X)
