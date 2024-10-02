import math
from datetime import date

def lj_calculate_tire_volume(width, aspect_ratio, diameter):

    diameter_mm = diameter * 25.4
    volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

    return volume

def main():
    
    width = int(input("Enter the width of the tire in mm (ex 205): "))
    aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

    volume = lj_calculate_tire_volume(width, aspect_ratio, diameter)

    current_date = date.today()

    print(f"The approximate volume is {volume:.2f} liters")

    buy_tires = input("Do you want to buy tires with these dimensions? (yes/no): ").lower()

    if buy_tires == "yes":
        phone_number = input("Please enter your phone number: ")
        with open("volumes.txt", "a") as file:
            file.write(f"{current_date}\t{width}\t{aspect_ratio}\t{diameter}\t{volume:.2f}\t{phone_number}\n")
        print(f"Thank you! Your phone number ({phone_number}) has been recorded.")

if __name__ == "__main__":
    main()

