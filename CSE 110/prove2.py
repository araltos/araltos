print("\n MadLib Game") 
star = input("\n Enter yes or no to continue the game: ")

if star in ['y', 'Y', 'yes', 'Yes', 'YES']:
    print("\n Please enter the following: \n")
else:
    exit()

adjetive = input("Adjective: ")
noun = input("Noun: ")
emotion = input("Emotion: ")
adjetive2 = input("Adjetive: ")
verb = input("Verb: ")
weather = input("Weather: ")
noun2 =input("Noun: ")
adjetiv3 =input("Adjetive: ")
noun3 = input("Noun: ")

Madlib = f"Hey! One {weather} day, I was walking in the main street, but {adjetive} {noun} stopped me and asked me where to find a {noun2}. I answered him: {emotion} maybe 3 streets up there should be a {adjetive2} {noun3}. When the {noun} {verb} to the {noun2}. An {adjetiv3} apple just fell from the sky and the {noun} said: That is what i needed!."

print(Madlib)