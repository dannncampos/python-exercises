# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math, random

num = float(input('Digite um número real, por exemplo 1.234: '))
print('O número que você digitou é {}, mas truncado ele ficaria {}.'.format(num, math.trunc(num)))
