num = int(input("Enter a number: "))
num2 = num
strt = 1
per = 1
for x in range((-num+1),num):
    if x > 0:
        per = 1
        for a in range(num+2):
            print(' ',end='')
        for b in range(strt-2):
            print(per,end=' ')
            per += 1
        strt -= 1
        num += 1
        print()
    else:
        per = 1
        for z in range(num):
            print(' ',end='')
        for y in range(strt):
            print(per,end=' ')
            per += 1
        strt += 1
        print()
        num -= 1

# input: 5

# output:
#      1 
#     1 2
#    1 2 3
#   1 2 3 4
#  1 2 3 4 5
#   1 2 3 4
#    1 2 3
#     1 2
#      1