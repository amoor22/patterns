num = int(input("Enter a number: "))
strt = 1
strts = num - 1
for x in range(num-1):
    print(" " * strts,"*" * strt)
    strts -= 1
    strt += 1
for z in range(num):
    print(" " * strts ,"*" * strt)
    strt -= 1
    strts += 1

# input: 5

# output:

#      *
#     **
#    ***
#   ****
#  *****
#   ****
#    ***
#     **
#      *