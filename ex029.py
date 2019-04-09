# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada km/h ultrapassado do limite de 80km/h.

v = float(input('A velocidade limite é 80km/h. \nDigite a velocidade que você passou: '))
lim = 80
multa = (float(7))
if v <= 80:
    print(f'Parabéns, com a velocidade de {v} km/h você não foi multado.')
else:
    print('Que coisa, não? Você foi multado em R$ {:.2f}. \nPreste mais atenção!'.format(multa*(v-lim)))