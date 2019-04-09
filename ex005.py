# 07/02/2019
# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

numero = int(input('Digite um número: '))
print('O número antes de {} é {}, e o número após {} é {}.'.format(numero, numero-1, numero, numero+1))