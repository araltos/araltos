age = int(input('\nWhat is the age of the first rider? '))
tall = int(input('What is the height of the first rider? '))
second_ride = input('Is there a second rider (yes/no)? ')

if second_ride.lower() == "yes":
    age_2 = int(input('What is the age of the second rider? '))
    tall_2 = int(input('What is the height of the second rider? '))
    if ((tall >= 36 and tall_2 >=36 and age >= 18) or (tall >= 36 and tall_2 >= 36 and age_2 >= 18)):
        print('Welcome to the ride. Please be safe and have fun!')
    else:
        print('Sorry, you may not ride.')
else:
    if age >= 18 and tall >= 36:
        print('Welcome to the ride. Please be safe and have fun!')
    else:
        print('Sorry, you may not ride.')


'''
age_2 = int(input('What is the age of the second rider? '))
tall_2 = int(input('What is the height of the second rider? '))

if (age >= 18 and tall >= 62):
    if second_ride.lower() == 'yes' or (age_2 >= 18 and tall_2 <= 36):
        if age_2 <=18:
            print('Welcome to the ride. Please be safe and have fun!')
        else:
            print('Sorry, you may not ride.')
'''