# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras ao todo sem considerar espaços
# Quantas letras tem o primeiro nome

n = str(input('Digite seu nome completo: ')).strip()
print('Em letras maiúsculas: \n', n.upper())
print('Em letras minúsculas: \n', n.lower())
nlt = len(''.join(n.split()))                    # Split para separar em cadeias, ''.join para juntar sem espaços
print('Quantas letras ao todo: ', nlt)            # Outro método: .format(len(nome) - nome.count(' '))
nlp = n.split()                                    # Separou em cadeiras
nlp = len(nlp[0])                                   # Quantidade de letras na primeira cadeia
print('Quantas letras tem o primeiro nome: ', nlp)

# Outro método: .format(nome.find(' ')) que é a casa onde tem o
# primeiro espaço, então o que tem pra trás é o primeiro nome.
