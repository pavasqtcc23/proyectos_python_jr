
'''Par o impar:
Lo primero que vamos a realizar es dar la bienvenida preguntando un número entre 1 y 1000
Cuando el usuario proporciona el número, comprobaremos si es par o impar y después imprimimos el mensaje con el resultado.
'''



from proyecto1_Par_Impar.esParImpar import *
from sys import float_repr_style

input("Bienvenido a este nuevo programa : presione **Start**")

numero = input("Ingrese un valor entre 1 a 1000: ")
numero = float(numero)


esPar(numero);





