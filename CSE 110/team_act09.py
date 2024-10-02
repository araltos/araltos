numbers = []
sum = 0
average = 0

print("Enter a list of numbers, type 0 when finished.")

while True: 
    number = int(input("Enter number: "))
    if number == 0:
        break
    numbers.append(number)
    sum += number
    average = sum / len(numbers)

print("The sum is: ", sum)
print("The average is: ", average)
print("The largest number is: ", max(numbers))