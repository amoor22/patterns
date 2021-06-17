num = int(input("Enter a number: "))
# Cheking if odd number
if num % 2 != 0:
    num += 1
for y in range(num + 1):
    for x in range(num + 2):
        if x == y or x + y == num:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# input: 7

# output:

# *       * 
#  *     *
#   *   *
#    * *
#     *
#    * *
#   *   *
#  *     *
# *       *