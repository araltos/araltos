import math

print("Welcome to the velocity calculator. Please enter the following: ")

mass = float(input("\nMass (in kg): "))
gravity = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
time = float(input("Time (in Seconds): "))
density = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
area = float(input("Cross sectional are (in m^2): "))
const = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

calculation = (1/2) * density * area * const 

velocity = math.sqrt(mass*gravity/calculation) * (1 - math.exp((-math.sqrt(mass*gravity*calculation) / mass) * time))

print(f"\nThe inner value of c is: {calculation:.3f}")
print(f"The velocity after 10.0 seconds is: {velocity:.3f} m/s")