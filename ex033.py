# Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
if n1 > n2:
   maior = n1
   menor = n2
else:
    maior = n2
    menor = n1
if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3
print(f'MAIOR número: {maior}\nMENOR número: {menor}')


