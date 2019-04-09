from Cores import cores
line = int(input('Size of the pyramid: '))
[print('_'*(line-i) + '\033[36m*\033[m'*(2*i+1) + '_'*(line-i)) for i in range(line+1)]