# 08/02/2019
#  Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

nprova = float(input('Insira a nota da prova: '))
ntrabalho = float(input('Insira a nota do trabalho: '))
pp = int(input('Qual o peso da prova? '))
pt = int(input('Qual o peso do trabalho? '))
nota = float(((nprova*pp)+(ntrabalho*(pt)))/(pp+pt))
print('Sua nota é: {:.2f}'.format(nota))