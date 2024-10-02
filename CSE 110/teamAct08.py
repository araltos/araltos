word = "Commitment"
result = ""
fav_letter= str(input('What is your favortite letter: '))

for i in word:
    if i == fav_letter:
        result += i.upper()
    else:
        result += i

print(result)