# 08/02/2019
#  Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

n = int(input('Digite um número: '))
print('A tabuada desse número é: \n',
      '-'*15,
      '\n {:2} x {:2} = {:2}'.format(n, 1, n * 1),
      '\n {:2} x {:2} = {:2}'.format(n, 2, n * 2),
      '\n {:2} x {:2} = {:2}'.format(n, 3, n * 3),
      '\n {:2} x {:2} = {:2}'.format(n, 4, n * 4),
      '\n {:2} x {:2} = {:2}'.format(n, 5, n * 5),
      '\n {:2} x {:2} = {:2}'.format(n, 6, n * 6),
      '\n {:2} x {:2} = {:2}'.format(n, 7, n * 7),
      '\n {:2} x {:2} = {:2}'.format(n, 8, n * 8),
      '\n {:2} x {:2} = {:2}'.format(n, 9, n * 9),
      '\n {:2} x {:2} = {:2}\n'.format(n, 10, n * 10),
      '-'*15)

