'''
week10.py
Sis Hansen
'''

#### review
nums = []  # empty list we can append to later
nums = [1,5,7,9]  # initialized list
print(f'the third item is: {nums[2]}') # using the index

# get the number of items in the list & print it
num_of_nums = len(nums)
print(num_of_nums)
print(len(nums))
print()
# loop through a list to print each item
for num in nums:
    print(num)

# loop through a list using the index (and range)
# print('\nprint with index')
for i in range(len(nums)): # creates collection -> 0,1,2,3
    # print(nums[i])
    print(f"at index {i} is {nums[i]}")



#### NEW
# loop thru list using index and user friendly (+1) display
print("\nuser friendly (don't print 0)")
for i in range(len(nums)):
    print(f"{i+1}. is {nums[i]}")

# use the index for 2 "parallel" lists
names = ['bill', 'jenny', 'tom']
ages = [9, 10, 8]
print('\nloop thru two lists to print both values')
for i in range(len(names)): # -> 0,1,2
    print(f"{names[i].capitalize()} is {ages[i]} year old.")


# index + 1 makes it more user friendly


# replace the second age 
print('\nages before changing 2nd item (index 1):', ages)
ages[1] = 29
print('ages after changing the 2nd item:', ages)

# ask the user which item they want to replace
# if I used user friendly numbers to display, 
# I need to -1 to get the correct index 
replace_item = int(input("Which of do you want to replace: ")) - 1
new_item = int(input("What age should it be: "))
ages[replace_item] = new_item

# show the list again to show the new age is in the list
print('\naltered list:', ages)


# remove an item from the nums list with pop()
nums = [1,5,7,9]  # initialized list
print('\nbefore popping from nums')
print(nums)
popped_num = nums.pop(1)
print('\nafter popping from nums')
print(nums)

# print the item removed (popped)
print(popped_num)





# print()

# BONUS: insert a value at index 1 (may confuse some)
# val = (input('Enter a value to insert at index 1: '))
# nums.insert(1, val)
# print('list with value inserted at index 1: ', nums)
# print()

