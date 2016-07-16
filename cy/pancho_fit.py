import numpy as np
def fit_poly(x,y,dy,n):
    V = np.asmatrix(np.diag(dy**2))
    M = []

    for k in range(n+1):
        M.append(x**k)
    M = np.asmatrix(M).T
    theta = (M.T*V.I*M).I*M.T*V.I*np.asmatrix(y).T
    cov_t = (M.T*V.I*M).I

    return np.asarray(theta.T)[0], np.asarray(cov_t)
