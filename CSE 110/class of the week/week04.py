'''
Week 04: Solving problems with variables and expressions
Sister Hansen

'''
import math

# f-strings (new vs old)
a = 100
b = 45
# new
print(f'This is a string with f-string formatting... {a + 5 * 23 - 12:.2f} {b} {"nice":&>10}')
# old
print('This is a string with .format formatting... {:.2f} {} {:&>10}'.format((a + 5 * 23 - 12), b, "nice"))
print()

# take a look at the formatting reference sheet
print(f'here\'s another example: {a:*^10.2f} and {b:#^20}')
print()

# calculate f = ma  (force = mass * acceleration)
mass = float(input("Mass (kg): "))
accel = float(input('Acceleration (m/s^2): '))
force = mass * accel
print(f"{force=}")  # cool trick to print variable=value

# print result formatted nicely and with 4 decimals
print(f'Force is {force:.4f} Newtons')
print()

# what do I do if there's a function in the math module
# that I need to use?
x = 10 ** .5
print(x)
y = float(input('Enter a number to take the square root of: '))
sqrt_of_y = math.sqrt(y)
print(f'The square root is: {sqrt_of_y:.3f}')
