from Cores import cores
def pyramid(rows):
  result = ''

  for i in range(rows):
    row = ''
    row += '_' * (rows - i - 1)
    row += '*' * (2 * i + 1)
    row += '_' * (rows - i - 1)

    result += row + '\n'

  return result
rows = int(input("Quantidade de linhas: "))

print (pyramid(rows))