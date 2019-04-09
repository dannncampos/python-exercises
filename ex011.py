# 08/02/2019
# Faça um programa que leia a área de uma parede em metros quadrados,
# sabendo que um litro de tinta pinta uma área de 2m², quantos litros são necessários?

ap = float(input('Qual a altura da parede em metros? '))
lp = float(input('Qual a largura da parede em metros? '))
p = ap * lp
rt = float(input('Qual o rendimento da tinta em litros por m²? '))
print('Sua parede de {} m x {} m tem {:.2f} m².\n'.format(ap,lp,p),
      'Você irá precisar de {:.1f} litros de tinta para pintar a área de {:.2f} m².'.format(p/rt, p))