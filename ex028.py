# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
from random import randint
from time import sleep
numpc = randint(0, 5) # Computador sorte de 0 a 5.
print('-=-'*20)
mensagem = 'Tente adivinhar o número que escolhi!'
print(f'{mensagem:^60}')
print('-=-'*20)
numu = int(input('\nDigite um número de 0 a 5: '))
print('PROCESSANDO...\n')
sleep(2)
print('Você acertou!' if numu == numpc else 'Você errou! O número foi << {} >>'.format(numpc))