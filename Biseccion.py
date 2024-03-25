# %% Método de Bisección
'''
i: numero de iteraciones del método
E: error del método, calcula el error entre $ (P_n - Pn-1)/Pn $
Delta: calcula la diferencia entre la función y el cero
Alfa: parámetro que me ayuda a determinar la variación del error $ E/alfa $
Epsilon: es el "cero" de la maquina
''' 

# %% Reset
# from IPython import get_ipython
# get_ipython().magic('reset -sf')

# %% Librerías
import pandas as pd
import json

# %% Funciones
import Funciones_Biseccion as f

# %% Entradas
print("\nMétodo de Bisección\n")

#Archivo con las entradas
archivo = input("¿Tiene un archivo de texto con las entradas? y/n\n")
tipDoc = input("Escoja el tipo de archivo, 1:.txt, 2:json\n")

if archivo == "y":
    if tipDoc == "1":
        ##Archivo de texto
        entradas = open("Entradas.txt","r")
        entradas1 = entradas.readlines()
        entradas.close()
        del(entradas)
        
        entradas1 = list(map(float,entradas1))
        a = entradas1[0]
        b = entradas1[1]
        TOL = entradas1[2]
        tipErr = entradas1[3]
        No = entradas1[4]
        del(entradas1)
        
    else:
        #Archivo tipo json
        with open("Entradas.json","r") as entradas:
            entradas1 = json.load(entradas)
            del(entradas)
            
            a = entradas1["a"]
            b = entradas1["b"]
            TOL = entradas1["TOL"]
            tipErr = entradas1["tipErr"]
            No = entradas1["No"]
            del(entradas1)

#MIngreso manual de las entradas
else:
    print("Ingrese los limites del intervalo [a,b]")
    a = float(input("Valor de a\n"))
    b = float(input("Valor de b\n"))
    TOL = float(input("Ingrese el valor de la tolerancia(TOL)\n"))
    tipErr = int(input("Escoja el tipo de error, 1:E_abs, 2:E_rel, 3:E_%\n"))
    No = int(input("Ingrese el numero máximo de iteraciones(No)\n"))
    
#Guardar resultado
guardar = input("¿Quiere guardar el resultado? y/n\n")
r_anterior = input("¿Mostrar resultado anterior? y/n\n")

# %% Declaración de variables
i = 1
E = 100.0
alfa = 1.0
delta = 100.0
epsilon = 2.2250738585072014e-308
Linf = a
Lsup = b
z = a
FA = f.fp(a)
resultados = []
resultado_anterior = []
a1 = "a(-)"
b1 = "b(+)"
aux = ""
Err = ''
FP = 0
p = 0
texto_resultado = f'''\n[a,b] = [{Linf},{Lsup}]
p = {p}
f(p) = {FP}
Error{Err}{tipErr} = {E}
Alfa = {alfa}
Delta = {delta}
TOL = {TOL}
No = {i}
{'-'*61}'''

# %% Consideraciones iniciales
if TOL == 0.0:
    TOL = epsilon

if  1 < tipErr < 3:
    tipErr = 2
    
if FA > 0:
    a1 = "a(+)"
    b1 = "b(-)"

#Tipo de error(salida)    
if tipErr == 1:
    Err = "_abs"
elif tipErr == 2:
    Err = "_rel"
elif tipErr == 3:
    Err = "_%"
    
# %% Método de Bisección
while E> epsilon and i<=No:
    p = (a+b)/2.0
    FP = f.fp(p) 
    
    if p != 0.0:
        E = f.Errores(tipErr,p,z)
        
    if (FP != 0.0)and(i > 1):
        delta = f.Errores(2,FP,resultados[i-2][3])
        
    alfa = abs(E/alfa)
        
    resultados.append([a,b,p,FP,E,alfa,delta,TOL])
        
# %% Impresión y almacenamiento de resultados
    
    #Resultado actual
    if (FP==0.0)or(delta<TOL):
        print(f'{'-'*61}\nProceso exitoso\nDatos de la ultima iteración:')
        print(texto_resultado)
        
        #Resultado anterior   
        if r_anterior == "y":
            resultado_biseccion = open("resultado_biseccion.txt","r")
            resultado_anterior = resultado_biseccion.readlines()
            resultado_biseccion.close()
            del(resultado_biseccion)
             
            print("Ultimo resultado guardado\n")
            
            for i in range(len(resultado_anterior)-9,len(resultado_anterior)-1):
                aux = aux + (str(resultado_anterior[i]))
                 
            print(f'{aux}{'-'*61}')
    
        #Archivo de texto con los datos
        if guardar == "y":
            resultado_biseccion = open("resultado_biseccion.txt","a")
            resultado_biseccion.write(texto_resultado)
            resultado_biseccion.close()
            del(resultado_biseccion)
            
            #Creación del Data Frame
            df_resultados = pd.DataFrame(resultados,
                columns=[a1,b1,"p","f(p)","Error"+Err,"Alfa","Delta","TOL"])
            del(resultados)
            
            #Archivo de excel con los datos de las iteraciones
            df_resultados.to_excel("Datos_Biseccion.xlsx")
            
        break    

    #Actualización del intervalo
    if FA*FP > 0.0:
        a = p
        FA = FP
    else:
        b = p  
    
    i += 1    
    z = p
    alfa = E
    
if i > No:
    print("\nEl método ha fallado luego de la iteración No =", i-1)    