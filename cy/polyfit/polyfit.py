from time import time
from polyC import poly_c , poly_cc
import numpy as np
X=np.arange(1,1000,dtype=np.float64)
Y=3*(X+np.random.random(999))
sigma=np.array([Y.std() for i in range(999)],dtype=np.float64)
t0=time()
poly_c(X,Y,sigma,4)
print("{}".format(time()-t0))
