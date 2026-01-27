# Example 1 => if/elif/else

# num = 10
# if num > 0:
#     print("positiv")
# elif num == 0:
#     print("zero")
# else:
#     print("negative")
    
    
# Example 2 => nested if

# age = 25

# if age > 18:
#     if age < 30:
#         print("young")
#     else:
#         print("adult")
# else:
#     print("kid")

# Example 3 => for loop

# fruits = ["apple", "banana", "orange"]

# for fruit in fruits:
#     print(fruit)

# Example 4 => for loop range

# for i in range(10):
#     print(i)

# Example while

# count = 7

# while count > 0:
#     print(count)
#     count = count - 1
    
# print('outside of while')

# Example with break

# for i in range(10):
#     if i == 5:
#         break;
#     print(i)

# print('Outside')

# Example for with continue

# for i in range(10):
#     if i == 5 or i == 4:
#         continue
#     print(i)

# print('outside')

# Example odd numbers
# for i in range(10):
#     if i%2 == 0:
#         continue
#     print(i)
# print('outside')

# Example even numbers
for i in range(10):
    if i%2 != 0:
        continue
    print(i)
print('outside') 
    