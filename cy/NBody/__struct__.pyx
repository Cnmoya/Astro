import numpy as np
cimport numpy as np
typedef Body struct:
  double[3] x
  double[3] v
  double m
cdef double g = 6.674 * 10 **-11
def avanzar(double dt, int n , bodies,nbodies):
  cdef int i,j
  for i in range(n):
    temp = bodies[i]
    xbody = nbodies[i]
    m1 = temp.m
    for j in range(n-1):
      cdef double r[3],F[3],m
      m2 = xbody[j].m
      r[1]=temp.x[1]-xbody[j].x[1]
      r[2]=temp.x[2]-xbody[j].x[2]
      r[3]=temp.x[3]-xbody[j].x[3]
      F[1] = g*(m1*m2)/(r[1]**2)
      F[2] = g*(m1*m2)/(r[2]**2)
      F[3] = g*(m1*m2)/(r[3]**2)
