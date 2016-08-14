__author__ = "Michael Haacke"


from math import pow
from functools import reduce
from itertools import chain


def sumar_con_error(valor_fun_a,error_a,*args):
    #funcion  que calcula la propagacion de errores de la suma en una funcion sin corelacion
    valor_f_f = valor_fun_a + sum((float(args[i]) for i in range(0,len(args),2)))
    error_f_f = pow(pow(error_a,2) + sum((pow(args[i],2) for i in range(1, len(args), 2))),1/2)
    return (valor_f_f,error_f_f)

def multiplicacion_con_error(valor_fun_a,error_a,*args):
    #funcion  que calcula la propagacion de errores de una de una multiplicacion de funcion sin
    # corelacion
    valor_f_f = valor_fun_a * reduce(lambda x,y:x*y,(float(args[i]) for i in range(0,len(args),2)))
    if valor_f_f == 0:
        return  (0,0)
    else:
        error_f_f = pow(sum((pow(args[i]/args[i-1],2) for i in range(1,len(args), 2)))+pow(
            error_a/valor_fun_a,2),1/2)
        return (valor_f_f,error_f_f*valor_f_f)

def division_con_error(valor_fun_a,error_a,*args):
    #funcion  que calcula la propagacion de errores de una de una division de funcion sin
    # corelacion
    valor_f_f = valor_fun_a * reduce(lambda x,y:x*y,(pow(float(args[i]),-1) for i in
                                                                     range(0,len(args),2)))
    if valor_f_f == 0:
        return  (0,0)
    error_f_f = pow(sum((pow(args[i]/args[i-1],2) for i in range(1,len(args), 2)))+pow(
        error_a/valor_fun_a,2),1/2)
    return (valor_f_f,error_f_f*valor_f_f)


def elevacion_exacta(valor_fun_a,error_a,elevado):
    valor_f_f = pow(valor_fun_a,elevado)
    error_f_f = abs(elevado*error_a/valor_fun_a*valor_f_f)
    return (valor_f_f,error_f_f)


if __name__ == '__main__':
    print(sumar_con_error(0,0,0,0,0))
    print(multiplicacion_con_error(10,0,1,0.5))
    print(division_con_error(10, 0, 1, 0.5))
    print(elevacion_exacta(10,5, 2))
