num = int(input("Enter a number: "))
has = 1
for x in range(num):
    for y in range(num):
        # 2 spaces and add a space after # and *
        print('  ',end='')
    for i in range(has):
        if i % 2 == 0:
            print('* ',end='')
        else:
            print('# ',end='')
    print()
    has += 2
    num -= 1

# input: 7

# output:

#               * 
#             * # *
#           * # * # *
#         * # * # * # *
#       * # * # * # * # *
#     * # * # * # * # * # *
#   * # * # * # * # * # * # *