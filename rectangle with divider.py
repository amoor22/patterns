height = int(input('Height: '))
width = int(input('Width: '))
print()
for x in range(1,height + 1):
    for y in range(1,width+1):
        if x == 1 or y == 1 or y == width or x == height:
            print('* ',end='')
        elif y == width // 2 and width % 2 == 0:
            print(' *',end='')
        elif y == (width // 2) + 1 and width % 2 != 0:
            print('* ',end='')
        else:
            print('  ',end='')
    print()

# input:
#  6
#  8

# output:

# * * * * * * * *
# *      *      *
# *      *      *
# *      *      *
# *      *      *
# * * * * * * * *