# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens até 200km e R$ 0,45 para viagens mais londas.

dv = float(input('Qual a distância da viagem em km? '))
cmaior = float(0.50)
cmenor = float(0.45)
print(f'Para {dv} km:')
print('Passagem: R$ {:.2f}.'.format(dv*cmaior) if dv <= 200 else 'Passagem R$ {:.2f}.'.format(dv*cmenor))