num = int(input("How big do you want the cake? "))
num2 = 2
for x in range(num):
    for y in range(2):
        for i in range(num * 2 - 2):
            print(' ', end='')
        for a in range(num2):
            print('*',end='')
        if y == 0:
            print()
    num2 += 4
    num -= 1
    print()

# input: 4

# output:
#       **
#       **
#     ******
#     ******
#   **********
#   **********
# **************
# **************