# Funciones_Biseccion

# %% Librerías
import math

# %% Funciones a evaluar
def fp(p:float)->float:
    '''
    Evalúa la función programada en el parámetro indicado.
    '''

    f = p**(0.5)+(8**0.5)*p-(8**0.5)
    #f =  10*p+10
    #f = math.sqrt(p)-math.cos(p)
    #f = (p**3)+4*(p**2)-10
    #f = p-2*(math.sin(p))
    #f = p-math.tan(p)
    #f = math.exp(p)-2-math.cos(math.exp(p)-2)
    #f = -12.4+10*(0.5*math.pi-math.atan(p)-p*(1-p**2)**1/2)
    #f = -1.7-((32.17)/(2*p**2))*(math.sinh(p)-math.sin(p))
    return f

# %% Errores
def Errores(tipErr: int, p:float, z:float)->float:
    '''
    Calcula el tipo de error pedido, entre los dos argumentos ingresados.
    '''

    if tipErr == 1:
        E = abs(p-z)
    elif tipErr == 2:
        E = abs((p-z)/(p))
    elif tipErr == 3:
        E = abs((p-z)/(p))*100.0
    return E