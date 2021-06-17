num = int(input("Enter a number: "))
one = 1
num2 = 1
asterisk_list_odd = []
asterisk_list_even = []
last_odd = []
for x in range(num):
    for space in range(num):
        print(' ',end='')
    for i in range(num2):
        if num2 % 2 == 0:
            even_start = last_odd[-1] + num2
            print(even_start,end='')
            asterisk_list_even.append('*')
            if num2 > 1 and len(asterisk_list_even) < num2:
                print('*',end='')
            last_odd[-1] -= 1
        else:
            print(one,end='')
            asterisk_list_odd.append('*')
            if num2 > 1 and len(asterisk_list_odd) < num2:
                print('*',end='')
            last_odd.append(one)
        one += 1
    print()
    asterisk_list_odd.clear()
    asterisk_list_even.clear()
    num2 += 1
    num -= 1

# input: 4

# output:

#     1
#    3*2
#   4*5*6
#  10*9*8*7