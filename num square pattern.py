num = int(input('Enter a number: '))
for x in range(num):
    for y in range(num):
        if y >= x:
            print(num - x,end=' ')
        else:
            print(num - y,end=' ')
    print()

# input: 7

# output:
# 7 7 7 7 7 7 7 
# 7 6 6 6 6 6 6
# 7 6 5 5 5 5 5
# 7 6 5 4 4 4 4
# 7 6 5 4 3 3 3
# 7 6 5 4 3 2 2
# 7 6 5 4 3 2 1