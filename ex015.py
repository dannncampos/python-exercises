# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por Km rodado.

dialocado = int(input('Digite a quantidade de dias da locação do veículo: '))
qtdkm = float(input('Digite quantos Km o veículo rodou neste período: '))
diaria = float(input('Digite o preço da diária do veículo: R$ '))
valorkm = float(input('Digite o preço do Km rodado: R$ '))
print('O veículo foi alugado por {:.0f} dias. \nRodou {:.0f} km no período. \nCusto da diária é de R$ {:.2f}. \n'
      'O total a ser pago é: R$ {:.2f}.'.format(dialocado, qtdkm, diaria,dialocado*diaria+qtdkm*valorkm))