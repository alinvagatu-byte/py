# Exercise Factorial number

num = int(input("Enter a number: "))
result = 0

if num < 0:
    print('Impossible to calculate factorial')

if num == 0 or num == 1:
    print('Result is 1')

while num >= 1:
    predecesor = num - 1
    if result == 0:
        result = num
    else:
        result = result * num
    num = predecesor
    
if result > 0:
    print (f"Result is {result}")