#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

if len(sys.argv) < 2:
    entrada = input("Debe informar un número o rango: ")
else:
    entrada = sys.argv[1]

if "-" in entrada:
    rango = entrada.split("-")
    desde = int(rango[0])
    hasta = int(rango[1])
    for i in range(desde, hasta + 1):
        print("Factorial", i, "! es", factorial(i))
else:
    num = int(entrada)
    print("Factorial", num, "! es", factorial(num))
