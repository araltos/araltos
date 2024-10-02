''' 
team activity - week 13
Sister Hansen

'''

# The def (function) does not need to be at the begginig of the code but needs to be before it will excecute. 

# import math

# #Square
# def compute_area_square(len_side):
#     area = len_side ** 2 
#     return area

# side = float(input("Enter the lenght of a side: "))
# square_area = compute_area_square(side)
# print(square_area)

# #Rectangle
# def compute_area_rectangle(lengh, width):
#     area_rectangle = lengh * width
#     return area_rectangle

# length = float(input("What is the length of rectangle? "))
# width = float(input("What is the width of the rectangle? "))
# rectangle_are = compute_area_rectangle(length, width)
# print(rectangle_are)

# #Circle
# def compute_radius_circle(radius):
#     radius_circle = radius * radius * math.pi 
#     return radius_circle

# radius = float(input("What is the radius of the circle? "))
# circle_radius = compute_radius_circle(radius)
# print(f"{circle_radius:.1f}")


# In class Dec 6 2023
def say_hello(name1, name2 = "Julee", name3 = "Jann"):
    print(f"Hello {name1}, {name2}, and {name3}, how are you?")
    return "Jay"
name4 = "Theola"

def main():
    say_hello(name3 = "bill", name1 = "larry", name2 = "todd")
    say_hello("Lyle", "Dave")
    say_hello("Jolene")
    print(name4)
    # You can not use a value that is in a def value.
    # print(name3) name 3 is not in scope

main()

result = say_hello("Jim")
print(result)

 
# wind_chill = 35.74 + 0.621*T - 35.75*(V**0.16) + 0.4275*T*(V**0.16)

# write a function to calculate windchill if given tempF and velocity

# write a function to convert from C to F

# ask the user for a temperature
# ask the user if the temp iw in F or C
# if the temp is in C, convert to temp in F

# loop from 5 to 60 in increments of 5 (velocity)
    # call the winchill function, passing in velocity and tempF
    # print the result in nice fashion with 2 decimals

                #                  5      61     5
# function  for Velocity in range(Start, Stop, Increment): --> (Start, Starting,.... Stop)
