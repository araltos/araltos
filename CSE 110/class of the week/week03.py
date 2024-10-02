'''
Week 3: Variables and Expressions(math)
Sister Hansen
'''
# command + / = to make comment fast
#### Which are each of the following? (string, int, float)
x = '10' #string
y = 5    #int
z = 3.14 #float
# print(x*5, y, z*2) 

#### What do the following do?
x = int(x)    #int converte to integer a string value
y = float(y)  #turn to a float value. in this case turn a int to a float
z = str(z)    #turn in to a string value. 

# print(x, y, z*2)

#### Which is better?
# print("I have " + str(x) + " cats.")
# print("I have", x, "cats.")
# print(f"I have {x} cats.") #f funtion


#### Order of operations
#### math operations and order of operations
'''
Operator	Description
()	        Parentheses
**	        Exponent
* / // %	Multiply, Divide, Floor divide, Modulo
+ -	        Addition, Subtraction
= 	        Assign
'''

#### What is stored in a, b, c and d? 
a = 10 + (4 * 2) - 3  #15 
b = 5 % 2             #1
c = 5 // 2            #2
d = 5 / 2             #2.1
e = 2 / 2             #
# print(f'math {a}, modulo {b}, floor divide {c}, normal divide {d}')

#### Team Activity
## Core requirements: 
# get user input (be able to handle ints or floats)
# convert it to a number so you can do some math with it (float)
# calculate areas of 3 shapes

# side = ???(input('What\'s the length of one side: '))
# it is safe to use better float than integer because if the user type 1 or 1.0 i will still do not have problem if is a float
