# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
# sobre ele.

c = input("Digite algo aqui: ")
print('"{}" é uma string? R.:'.format(c), c.isalpha())
print('"{}" é um número? R.: '.format(c), c.isnumeric())
print('"{}" ESTÁ EM LETRA MAIÚSCULA? R.: '.format(c), c.isupper())
print('{} está em letra minúscula? R.: '.format(c), c.islower())
print('{} está capitalizada? R.: '.format(c), c.istitle())
print('O tipo de "{}" é: '.format(c), type(c))