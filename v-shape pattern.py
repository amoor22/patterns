num = int(input("Enter a number: "))
noom = num-1
num2 = 0

while noom > 0:
    for x in range(num2):
        print(' ',end='')
    print('*',end='')
    for x in range(noom):
        print(' ',end='')
    for x in range(noom -1):
        print(' ',end='')
    print('*')
    noom -= 1
    num2 += 1
    # last iteration
    if noom == 0:
        print(" " * (num2-1) , "*")

# input: 6

# output:

# *         *
#  *       *
#   *     *
#    *   *
#     * *
#      *