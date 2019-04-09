# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome SANTO

cidade = str(input('Digite o nome da cidade: ')).strip()
cidadeup = cidade.upper()
cidadeup = cidadeup.split()
print('O nome da cidade {} começa com SANTO? {}'.format(cidade, 'SANTO' in cidadeup[0:5]))

# Outra maneira: cidade[:5].upper() == 'SANTO' para mostrar os primeiros caracteres e comparar com SANTO.