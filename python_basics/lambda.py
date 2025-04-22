# Welcome to lambda note


# lambda is a function with no name 

#when to use lambda: sort the list, when using map, filter, without using def ....



# map() changes each item one by one  change each item 

# filter() picks only the items you need   keep only what you want  

# sort() puts items in order   Arrange items in order  









lambda x: x + 1

# same as 

def add_one(x):
    return x+1


print(add_one(5)) #x = 5 , 5+1 = 6








numbers = [5,2,9,1]
sorted_numbers = sorted(numbers, key=lambda x: x)
print(sorted_numbers) #[1,2,5,9]

people = [
       {"name": "Pucca", "age": 34}. {"name": "Garu", "age": 37}
]

#sort by age 

people.sort(key=lambda person: person["age"])


numbers = [1,2,3,]
doubled = list(map(lambda x: x * 2, numbers))

#Take every number x and return x * 2
#instead of 

def double(x): return x * 2

nums = [1,2,3,4,5,6,7,8,9,10]
even = list(filter(lambda x: x % 2 ==0, nums))

#keep the numbers that are even."

# 1. sort + lambda → "How should I sort?"
names = ["chloe", "Brian", "alex"]

# Sort ignoring case (normally capital letters go first)
names_sorted = sorted(names, key=lambda x: x.lower())
print("Sorted names:", names_sorted)

# 2. map + lambda → "How should I change each item?"
numbers = [1, 2, 3]
# Multiply each number by 10
multiplied = list(map(lambda x: x * 10, numbers))
print("Multiplied:", multiplied)

# 3. filter + lambda → "Which ones should I keep?"
nums = [1, 2, 3, 4, 5]
# Keep only numbers greater than 3
filtered = list(filter(lambda x: x > 3, nums))
print("Filtered:", filtered)





