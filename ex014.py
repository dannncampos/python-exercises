# Escreva um programa que converta uma temperatura digita em ºC e converta para ºF.

grausc = float(input('Qual a temperatura em graus Celsius? ºC '))
grausf = grausc*1.8+32
print('Temperatura em Celsius: {:.1f}'.format(grausc), ' ºC',
      '\nTemperatura em Farehneit: {:.1f}'.format(grausf), ' ºF')