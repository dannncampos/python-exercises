rows = int(input('How many rows are in it? ')) # The size of the pyramid
[print("_"*(rows-i-1) + "*"*(2*i+1) + "_"*(rows-i-1)) for i in range(rows)]
