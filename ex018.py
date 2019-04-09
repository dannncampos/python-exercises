# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, cos, sin, tan
a = float(input('Insira o ângulo: '))
sin = sin(radians(a))
cos = cos(radians(a))
tan = tan(radians(a))
print(f'Ângulo {a:3}º \nSeno: {sin:.6f} \nCosseno {cos:.6f} \nTangente: {tan:.6f}')