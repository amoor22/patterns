num = int(input("Enter a number: "))
strt = 1

for x in range(num-1):
    print(str(strt) * strt)
    strt += 1
for z in range(num):
    print(str(strt) * strt)
    strt -= 1

# input: 6

# output:

# 1
# 22
# 333
# 4444
# 55555
# 666666
# 55555
# 4444
# 333
# 22
# 1