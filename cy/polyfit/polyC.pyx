cimport numpy as np
import numpy as np
cimport cython
from functools import reduce as rr
@cython.boundscheck(False)
@cython.wraparound(False)
cpdef np.ndarray[np.float64_t, ndim=1] poly_c(np.ndarray[np.float64_t, ndim=1] x ,
 np.ndarray[np.float64_t, ndim=1] y , np.ndarray[np.float64_t, ndim=1] dy , np.int n):
  cdef np.ndarray[np.float64_t, ndim=2] V, M , C
  V=np.asmatrix(np.diag(dy**2),dtype=np.float64)
  M=np.asmatrix(x[:,None]**np.arange(n+1),dtype=np.float64)
  C=rr(np.dot,[M.T,V.I,M]).I
  C1=rr(np.dot,[C,M.T,V.I,np.asmatrix(y).T])
  return C1[0]
