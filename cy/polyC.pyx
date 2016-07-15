cimport numpy as np
import numpy as np
ctypedef np.double_t[:] D1
ctypedef np.double_t[:,:] D2
cpdef poly_c(D1 x , D1 y , D1 dy , np.int n):
  cdef D2 V,M
  V=np.asmatrix(np.diag(y),dtype=np.float64)
  M=np.asmatrix([np.asarray(x)**k for k in range(n+1)],dtype=np.float64)
  return V,M
