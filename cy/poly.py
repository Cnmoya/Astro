import numpy as np
from polyC import poly_c
from time import time
x=np.arange(1,1000)
x=np.asarray(x,dtype=np.float64)
y=3*x+np.random.random(999)
y=np.asarray(y,dtype=np.float64)
dy=np.array([y.std() for i in range(1,1000)],dtype=np.float64)
t0=time()
a,b=poly_c(x,y,dy,4)
print("tiempo fue {}s".format(time()-t0))
