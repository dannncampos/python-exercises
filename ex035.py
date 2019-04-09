# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
from Cores import cores
print('-=-'*15)
msg = 'Analisador de triângulo'
print('{:^45}'.format(msg.upper()))
print('-=-'*15)
r1 = float(input('Insira o lado 1: '))
r2 = float(input('Insira o lado 2: '))
r3 = float(input('Insira o lado 3: '))
if r1 < r2+r3 and (r1)**2 > (r2-r3)**2:
    print('{} Pode formar um triângulo! {}'.format(cores['azul'], cores['limpa']))
else:
    print('{} Não pode formar um triângulo! {} '.format(cores['azul'], cores['limpa']))


