# 08/02/2019
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input('Digite o salário do funcionário em reais: R$ '))
a = int(input('Digite quantos por cento de aumento você quer: % '))
ns = (s)*(1+a/100)
print('Salário atual: R$ {:.2f}\nAumento: {} %\nNovo salário: {:.2f}'.format(s, a, ns))