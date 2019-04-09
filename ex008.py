# 08/02/2019
#  Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input('Digite a quantidade de metros: '))
print('Centímetros: {:.0f} cm\nMilímetros: {:.0f} mm'.format(m*100,m*1000))