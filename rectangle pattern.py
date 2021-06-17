height = int(input('Height: '))
width = int(input('Width: '))
for x in range(height):
    for y in range(width):
        if y == 0 or x == 0 or x == height-1 or y == width - 1:
            print('*',end=' ')
        else:
            print('  ',end='')
    print()

# input:
#  4 
#  7

# output:

# * * * * * * * 
# *           *
# *           *
# * * * * * * *