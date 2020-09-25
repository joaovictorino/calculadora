#!/bin/python3

import math
import os
import random
import re
import sys
from calculadora import Calculadora


if __name__ == '__main__':
    print("Informe as operações habilitadas (+) soma (-) subtração (*) multiplicação (/) divisão:")
    operadores = input()
    continuar = "S"
    teste = Calculadora(operadores)
    while continuar == "S":
        print("Informe valor 1:")
        valor1 = int(input())
        print("Informe valor 2:")
        valor2 = int(input())
        print("Informe a operação:")
        operador = input()
        resultado = teste.calcular(valor1, valor2, operador)
        print("Resultado: " + str(resultado))
        print("Desejar continuar? S/N")
        continuar = input()
