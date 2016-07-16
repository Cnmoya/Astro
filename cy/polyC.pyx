cimport numpy as np
import numpy as np
cimport cython
@cython.boundscheck(False)
@cython.wraparound(False)
cpdef poly_c(np.ndarray[np.float64_t, ndim=1] x ,
 np.ndarray[np.float64_t, ndim=1] y , np.ndarray[np.float64_t, ndim=1] dy , np.int n):
  cdef np.ndarray[np.float64_t, ndim=2] V, M
  V=np.asmatrix(np.diag(dy**2),dtype=np.float64)
  M=np.asmatrix(x[:,None]**np.arange(n+1),dtype=np.float64)
  return ((M.T*V.I*M).I*M.T*V.I*(np.asmatrix(y).T))[0],(M.T*V.I*M).I
