num = int(input("Enter a number: "))
numa = num
num2 = 0
for x in range(num-1):
    print("*" * num ," " * num2," " * num2, "*" * num,sep="")
    num -= 1
    num2 += 1
for x in range(numa):
    print("*" * num, " " * num2, " " * num2, "*" * num, sep="")
    num += 1
    num2 -= 1

# input: 7

# output:
# **************
# ******  ******
# *****    *****
# ****      ****
# ***        ***
# **          **
# *            *
# **          **
# ***        ***
# ****      ****
# *****    *****
# ******  ******
# **************