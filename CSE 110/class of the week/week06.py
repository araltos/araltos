'''
Week 6: Decisions (and Booleans and complex conditions)
Sis Hansen
'''

credits = 110
gpa = 2.0 # fload(input('Enter your gpa: '))

#### Boolean variables can be assigned directly
can_graduate = True  # should be True or False to be a boolean

# write an expression to determine what the value of can_graduate
# should be if you can graduate if you have 120+ credits and a gpa above 2.0
#can_graduate = None  # replace None with a condition (or complex condition)
can_graduate = credits >= 120 and gpa >= 2.0 #complex condition
print(can_graduate)

# Note: a good boolean variable name will indicate that it only has two possible values (T/F)

#### Logical operators (and, or, not) and complex conditions
# be careful with complex conditions (ones with and/or)
x = 4
y = x == 5 or 2  # this doesn't work the way you probably think it will
print(f'{y=}')
y = x == 5 or x == 2  # this works!
print(f'{y=}')


# logical operators have an order of operations too 
# not, and, or - see table

meal = "sandwich"
money = 0

if meal == ("sandwich" or meal == "pizza slice") and money > 5: # you need to be careful with waht you want to ejecute first. the same principles as what mathematical operation should be first it need to be between parentesis. 
    print("Your order will be ready in 5 minutes.")
else:
    print("Sorry, can't complete your order.")