import numpy as np
from polyC import poly_c
from time import time
from pancho_fit import fit_poly
#pancho's the T.A,sup pancho
x=np.arange(1,2000)
x=np.asarray(x,dtype=np.float64)
y=3*x+np.random.random(1999)
y=np.asarray(y,dtype=np.float64)
dy=np.array([y.std() for i in range(1,2000)],dtype=np.float64)
n=50
t0=time()
a,b=poly_c(x,y,dy,n)
#a,b=fit_poly(x,y,dy,n)
print("time={}s".format(time()-t0))
