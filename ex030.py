# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR

n = int(input('Digite um número inteiro: '))
print(f'O número {n} é IMPAR!' if n % 2 == 1 else f'O número {n} é PAR!')