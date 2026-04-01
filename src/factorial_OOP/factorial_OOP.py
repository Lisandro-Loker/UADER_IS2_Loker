#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

class Factorial:
    def __init__(self):
        pass

    def _calcular(self, num):
        if num < 0:
            return 0
        elif num == 0:
            return 1
        else:
            fact = 1
            while(num > 1):
                fact *= num
                num -= 1
            return fact

    def run(self, min, max):
        for i in range(min, max + 1):
            resultado = self._calcular(i)
            print("Factorial", i, "! es", resultado)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        entrada = input("Debe informar un número o rango: ")
    else:
        entrada = sys.argv[1]

    f = Factorial()

    if "-" in entrada:
        rango = entrada.split("-")
        desde = int(rango[0]) if rango[0] != "" else 1
        hasta = int(rango[1]) if rango[1] != "" else 60
        f.run(desde, hasta)
    else:
        num = int(entrada)
        f.run(num, num)