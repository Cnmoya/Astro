import numpy as np
#Hecho por Francisco Aros para el ramo AST0212
#Metodo de minimos cuadrados para una recta:
#    y = a*x + b
#que minimiza los residuos para encontrar
#los parametros a y b.
#Esta funcion recibe como variables numpy.arrays
#para x, y, dy. Siendo este ultimo los errores en y.
#como resultado entrega una lista con los parametros
#y sus errores ademas de el RMS y el factor de correlacion r^2
def fit_line(x,y,dy):
    S01 = np.sum(x**2/dy**2)
    S02 = np.sum(x/dy**2)
    S03 = np.sum(x/dy**2)
    S04 = np.sum(1.0/dy**2)
    S05 = np.sum(x*y/dy**2)
    S06 = np.sum(y/dy**2)

    det = (S01*S04 - S02*S03)
    A   = (S04*S05 - S02*S06)/det
    B   = (S01*S06 - S03*S05)/det
    dA  = np.sqrt(S04/det)
    dB  = np.sqrt(S01/det)

    RMS = np.sqrt(np.sum((y-A*x - B)**2/(float(x.size))))

    #calculo correlacion
    S21 = np.sum(x**2)
    S22 = np.sum(x)
    S23 = np.sum(x)
    S24 = x.size
    S25 = np.sum(x*y)
    S26 = np.sum(y)
    S27 = np.sum(y**2)

    A1  = (S24*S25 - S22*S26)/(S21*S24-S23*S22)
    A2  = (S24*S25 - S22*S26)/(S27*S24-S26*S26)
    ccf = np.sqrt(A1*A2)

    return A,dA,B,dB,RMS,ccf

#Este metodo realiza un fit con el metodo de minimos cuadrados
#pra un set de datos dado un polinomio de grado n:
#    y = a0 + a1*x**(1) +  a2*x**(2) + ... + an*x**(n)
#Recibe como parametros los datos x,y ademas del error en y
#como ultimo parametro es necesario incluir el orden del polinomio
#(por ejemplo n=1 para una recta)
#Como resultado entrega los coeficientes del polinomio en orden ascendente
#(a0,a1,a2,a3 ....) y la matriz de covarianza de los coeficientes
