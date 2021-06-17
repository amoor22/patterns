num = int(input("Enter a number: "))
col = 1
rew = 0
for x in range(num):
    rew = col
    print(col,end='')
    print(' ',end='')
    for y in range(col-1):
        if col > 1:
            rew += num
            print(rew,end=' ',sep='')
    print()
    col += 1

# input: 10

# output:
# 1 
# 2 12
# 3 13 23
# 4 14 24 34
# 5 15 25 35 45
# 6 16 26 36 46 56
# 7 17 27 37 47 57 67
# 8 18 28 38 48 58 68 78
# 9 19 29 39 49 59 69 79 89 
# 10 20 30 40 50 60 70 80 90 100