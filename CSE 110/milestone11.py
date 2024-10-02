
overall_max_life_expectancy = float('-inf')
overall_min_life_expectancy = float('inf')
overall_max_country = ""
overall_min_country = ""


user_year = int(input("Enter the year of interest: "))
user_max_life_expectancy = float('-inf')
user_min_life_expectancy = float('inf')
user_max_country = ""
user_min_country = ""
user_total_life_expectancy = 0
user_country_count = 0


with open('life-expectancy.csv') as file:
    
    next(file, None)

    
    for line in file:
        row = line.strip().split(',')

        try:
            current_year = int(row[2])  
        except ValueError:
            continue

        life_expectancy = float(row[3])  
        country = row[0]  

        
        if life_expectancy > overall_max_life_expectancy:
            overall_max_life_expectancy = life_expectancy
            overall_max_country = f"{country} in {current_year}"  

        if life_expectancy < overall_min_life_expectancy:
            overall_min_life_expectancy = life_expectancy
            overall_min_country = f"{country} in {current_year}"  

        
        if current_year == user_year:
            if life_expectancy > user_max_life_expectancy:
                user_max_life_expectancy = life_expectancy
                user_max_country = country

            if life_expectancy < user_min_life_expectancy:
                user_min_life_expectancy = life_expectancy
                user_min_country = country

            user_total_life_expectancy += life_expectancy
            user_country_count += 1


user_average_life_expectancy = user_total_life_expectancy / user_country_count if user_country_count > 0 else 0


print(f"\nThe overall max life expectancy is: {overall_max_life_expectancy:.3f} from {overall_max_country}")
print(f"The overall min life expectancy is: {overall_min_life_expectancy:.3f} from {overall_min_country}")


print(f"\nFor the year {user_year}:")
if user_country_count > 0:
    print(f"The average life expectancy across all countries was {user_average_life_expectancy:.2f}")
    print(f"The max life expectancy was in {user_max_country} with {user_max_life_expectancy:.2f}")
    print(f"The min life expectancy was in {user_min_country} with {user_min_life_expectancy:.3f}")
else:
    print("No valid data for the specified year.")

