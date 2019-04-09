# 08/02/2019
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print('# Use ponto ao invés de virgula para float!')
preco = float(input('Qual o preço do produto? R$ '))
desconto = int(input('Quanto você quer de desconto? % '))
print('Preço do produto: R$ {:.2f}\nDesconto: {} %\nTotal a pagar: R$ {:.2f}'.format(preco, desconto,))