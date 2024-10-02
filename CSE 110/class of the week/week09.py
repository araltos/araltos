'''
week09.py - Lists
Sister Hansen
'''
'''
ages =[12,10,2] ---> 12 10 2
                index 0 1 2'''
 
# A list is a COLLECTION!
# To create a list variable:
    # good_name = [ ] #empty list   OR...
    # good_name = [12, 10, 2] #initialized list

# create an empty list to hold names and an empty list to hold ages
names = []
ages = []

# recreate the names list to hold bill, tom, sue
names = ['bill', 'tom', 'sue']
print('names before appending', names)
# recreate the ages list to hold 12, 10, and 2
ages = [12,10,2]
print('ages before appending', ages)
# add an age (4) to the age list and jill to the name list
'''this is the way how to add to a variable informaion'''
ages.append(4)
names.append('jill')   
print('ages after appending', ages)
print('names after appending', names)

'''search python search function'''

''' 
remember that for loops are good at going through collections
for item in collection:
    do something each time we get an item (each time the loop iterates)
''' 
# use a for loop to go through the lists and print each item
# (2 ways)
for age in ages:
    print(age)
print() # MAKES SPACES BETWEEN LINES
for i in range(len(ages)): #collection -> 0,1,2,3... these are the indexes for the list
    print(i, ages[i])
# use the debugger to watch the value of name change


''' 
we can access each item in the list through an index
lists are stored in memory in adjacent memory buckets
                         _____________________
     ages -------------> | 12 | 10 |  2 |  4 |
                         ---------------------
                            0    1    2    3     index
'''
# print just the second item in the list
print(ages[1])
print(names[1])

# use a for loop to go through the ages list and
# add all the ages together for a total of all ages

totalOfages = 0
for age in ages:
    # total_of_ages = total_of_ages + age
    totalOfages += age # does the same thing as the line above
print('total is: ', totalOfages)

total_names = ""
for name in names:
    total_names += name
print(total_names)


#########################################
# day 2
#########################################
import random
# create a list of 15 random numbers (look up list comprehensions)  search for list comprehension...
nums = [random.randint(1,100) for x in range(15)]
print(nums)
print()

# find max value in the list (manually)
# need a variable to store the max when I find it
max_val = 0 
# need a loop to go thru the list to check for the max
for num in nums:
    if max_val < nums:
        max_val = num

print('max value is: ', max_val)
print()

# use a built-in function to find max
easy_max = max(nums)  # replace None
print('max value is: ', easy_max)
print()

# use a built-in function to find the min and sum
min_num = min(nums)         
total = sum(nums)
print(f'the min is {min_num}, the total is {total}')
print()

# create a new list that is sorted
print('original nums list:\n', nums)
sorted_nums = sorted(nums, reverse = True) # sort a list??
print(f'new sorted nums:\n {sorted_nums}')
print()

# sort the list "in-place"
print('original nums list:\n', nums)
nums.sort()
print('nums after sorting:\n', nums)
print()

# next week we'll see how to use indexes to 
# go through multiple lists in a for loop at once
