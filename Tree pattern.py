rows = int(input('Number of rows: '))
num1 = 1
num2 = rows

for x in range(rows):
    print(' ' * rows,"#" * num1)
    num1 += 2
    rows -= 1
print(' ' * num2,"#")

# input: 10

# output:

           #
          ###
         #####
        #######
       #########
      ###########
     #############
    ###############
   #################
  ###################
           #
