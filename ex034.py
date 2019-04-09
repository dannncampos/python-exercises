# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1250.00, calcule um aumento de 10%.
# Para os inferiores ou iguais o aumento é de 15%.

s = float(input('Digite o seu salário atual: R$ '))
print('Salário atual R$ {:.2f}\nNovo salário R$ {:.2f}'.format(s, s*1.15) if s <= 1250
      else 'Salário atual R$ {:.2f}\nNovo salário R$ {:.2f}'.format(s, s*1.10))