# # Import datetime so that it can be
# # used to compute a person's age.
# from datetime import datetime


# def main():
#     gender = input("Enter your gender (Male / Female): ")
#     b_day = input("Enter your Birthdate (YYYY-MM-DD): ")
#     weight = input("Enter your weight (U.S. pounds): ")
#     height = input("Enter your height (U.S. inches): ")
#     # Get the user's gender, birthdate, height, and weight.

#     # Call the compute_age, kg_from_lb, cm_from_in,
#     # body_mass_index, and basal_metabolic_rate functions
#     # as needed.

#     # Print the results for the user to see.
#     pass


# def compute_age(birth_str):
#     """Compute and return a person's age in years.
#     Parameter birth_str: a person's birthdate stored
#         as a string in this format: YYYY-MM-DD
#     Return: a person's age in years.
#     """
#     # Convert a person's birthdate from a string
#     # to a date object.
#     birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
#     today = datetime.now()

#     # Compute the difference between today and the
#     # person's birthdate in years.
#     years = today.year - birthdate.year

#     # If necessary, subtract one from the difference.
#     if birthdate.month > today.month or \
#         (birthdate.month == today.month and \
#             birthdate.day > today.day):
#         years -= 1

#     return years


# def kg_from_lb(pounds):
#     """Convert a mass in pounds to kilograms.
#     Parameter pounds: a mass in U.S. pounds.
#     Return: the mass in kilograms.
#     """
#     #Converts the weight from pounds to kilograms (1 lb = 0.45359237 kg).
#     conversion_w = 0.45359237
#     weight_kg = pounds * conversion_w

#     return weight_kg


# def cm_from_in(inches):
#     """Convert a length in inches to centimeters.
#     Parameter inches: a length in inches.
#     Return: the length in centimeters.
#     """
#     # Converts inches to centimeters (1 in = 2.54 cm).
#     conversion_l = 2.54
#     lenght_c = inches * conversion_l

#     return lenght_c


# def body_mass_index(weight, height):
#     """Compute and return a person's body mass index.
#     Parameters
#         weight: a person's weight in kilograms.
#         height: a person's height in centimeters.
#     Return: a person's body mass index.
#     """
#     return


# def basal_metabolic_rate(gender, weight, height, age):
#     """Compute and return a person's basal metabolic rate.
#     Parameters
#         weight: a person's weight in kilograms.
#         height: a person's height in centimeters.
#         age: a person's age in years.
#     Return: a person's basal metabolic rate in kcals per day.
#     """
#     return


# # Call the main function so that
# # this program will start executing.

from datetime import datetime

def main():
    # Ask the user to enter values
    gender = input("Enter your gender (M or F): ")
    b_day = input("Enter your Birthdate (YYYY-MM-DD): ")
    weight_lb = float(input("Enter your weight (U.S. pounds): "))  # Convert to float
    height_in = float(input("Enter your height (U.S. inches): "))  # Convert to float

    # Perform conversions and calculations
    age = compute_age(b_day)
    weight_kg = kg_from_lb(weight_lb)
    height_cm = cm_from_in(height_in)
    bmi = body_mass_index(weight_kg, height_cm)
    bmr = basal_metabolic_rate(gender, weight_kg, height_cm, age)

    # Print the results for the user to see.
    print(f"\nAge (years): {age}")
    print(f"Weight (kg): {weight_kg:.2f}")
    print(f"Height (cm): {height_cm:.1f}")
    print(f"Body mass index (BMI): {bmi:.1f}")
    print(f"Basal metabolic rate (BMR) (kcal/day): {bmr:.2f}")


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years

def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms."""
    conversion_w = 0.45359237
    weight_kg = pounds * conversion_w
    return weight_kg

def cm_from_in(inches):
    """Convert a length in inches to centimeters."""
    conversion_l = 2.54
    length_cm = inches * conversion_l
    return length_cm

def body_mass_index(weight, height):
    """Compute and return a person's body mass index."""
    bmi = (weight / (height ** 2)) * 10000
    return bmi

def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate."""
    if gender.lower() == 'm':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender.lower() == 'f':
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        raise ValueError("Invalid gender. Please enter 'M' or 'F'.")
    return bmr

# Call the main function
main()