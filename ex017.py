# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.

from math import hypot

ca = float(input('-- TRIÂNGULO RETÂNGULO -- \n Insira o comprimento da cateto adjacente: '))
co = float(input('Insira o comprimento do cateto oposto: '))
hi = hypot(ca, co)
print(f'Cateto Adjacente: {ca:.2f} m \nCateto Oposto: {co:.2f} \nHipotenusa: {hi:.2f} m')