## Copyright (C) 2018 SANTIAGO
## 
## This program is free software; you can redistribute it and/or modify it
## under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 3 of the License, or
## (at your option) any later version.
## 
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## 
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.

## -*- texinfo -*- 
## @deftypefn {} {@var{retval} =} biseccion (@var{input1}, @var{input2})
##
## @seealso{}
## @end deftypefn

## Author: SANTIAGO <SANTIAGO@LAPTOP-T90TB4HR>
## Created: 2018-02-23

function [S] = biseccion (a, b, epsilon, delta, Nmax)
## a y b es el intervalo en el que hay cambio de signo
## Epsilon es el error de la variable idependiente
## Delta va a ser el error de la funcion
## Nmax numero maximo de interacciones
## S es la matriz solucion
## S = interacciones, Xk, f(Xk), error

format long

E = 100; ## El error inicial
D = 100; ## Valor inicial para el delta
I = 0;## I contador de la interacciones
z = a;## Un calor para calcular el error que no tiene importancia
alfa = 1; ##Valor cualquiera para poder calcular la convergencia del metodo   
  while(E > epsilon && D > delta && I < Nmax)
   I = I +1;##Renovamos el contador
   S(I,1) = I; ##Almaceno I en la primera columna
   x = (a + b)/2; ##Calculamos la aproximacion de la x
   S(I, 2) = x; ##Almacenar la segunda columna
   y = funcion(x); ##Se evalua x en le fincion de arriba
   S(I, 3) = y; ##Almaceno la tercera columna
   D = abs(y); ##Se calcula el valor de f(x) y delta es la cota para el valor 
   ## de la funcion
   E = abs(x-z);##Error absoluto
   ##E = abs((x-z)/(x)); ##Error relativo
   ##E = abs((x-z)/(x))*100; ##Error porcentual
   alfa = E/(alfa); ##El alfa se calcula con el valor absoluto
   S(I,4) = E; ## Almaceno el error 
   S(I,5) = alfa; ##Almacenamiento en la quinta columna
   if funcion(a)* y < 0 ## si la funcion es negativa ahí esta la raíz
     b = x; ## redefinir el nuevo valor
     else
     a = x;
   endif
   z = x;
   alfa = E; 
  endwhile 

endfunction
