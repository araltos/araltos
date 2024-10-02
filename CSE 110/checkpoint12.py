people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

young_people = []

for person_str in people:
    person_info = person_str.split()
    print(f"Name: {person_info[0]} | Age: {person_info[1]}")

ages = [int(person.split()[1]) for person in people]
youngest_age = min(ages)

youngest_people = [person.split(" ")[0] for person in people if int(person.split(" ")[1]) == youngest_age]

# Append individual elements, not the entire list
young_people.extend(youngest_people)
young_people.append(youngest_age)

print()
print(f"The youngest person is: {young_people[0]} | Age: {young_people[1]}")

# print(f"The youngest person is: {young_people[0]} {young_people[1]}")
# print(f"The youngest person(s) is: {', '.join(youngest_people)}")


