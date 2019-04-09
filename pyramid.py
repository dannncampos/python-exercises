def pyramid(rows):
    result = ''
    for i in range(rows):
        row = '*'*(2*i+1)
        result += row.center(2*rows) + ('\n')
    return result
rows = int(input('Size of the pyramid: '))
print (pyramid(rows))
