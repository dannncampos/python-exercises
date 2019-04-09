# 08/02/2019
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. $1 = R$ 3,27

real = float(input('Quantos reais você tem? R$ '))
dolar = float(input('Qual o valor do dólar hoje? R$ '))
print('Você pode comprar $ {:.2f} com R$ {:.2f}'.format(real/(dolar), real))