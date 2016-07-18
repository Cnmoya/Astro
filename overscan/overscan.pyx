import numpy as np
import matplotlib.pyplot as plt
cimport numpy as np
cpdef void plot_os(np.ndarray[np.float64_t,ndim=2]data):
    cdef np.ndarray[np.float64_t,ndim=1] X,Y
    X=data.mean(axis=1)
    Y= np.arange(len(X))
    plt.plot(X,Y)
