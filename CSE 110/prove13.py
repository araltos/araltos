def calculate_wind_chill(temperature, wind_speed):
    return 35.74 + 0.6215 * temperature - 35.75 * wind_speed**0.16 + 0.4275 * temperature * wind_speed**0.16

def main():
    temperature = float(input("What is the temperature? "))
    unit = input("Fahrenheit or Celsius (F/C)? ").upper()

    if unit == "C":
        temperature = (temperature * 9/5) + 32

    for wind_speed in range(5, 65, 5):
        wind_chill = calculate_wind_chill(temperature, wind_speed)
        print(f"At temperature {temperature:.1f}F, and wind speed {wind_speed} mph, the wind chill is: {wind_chill:.2f}F")

if __name__ == "__main__":
    main()
