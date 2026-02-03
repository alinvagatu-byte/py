# Exercise odd/even number
import day3_odd_even_helper as oddEven

number = int(input("\nSelect a number: "))

isOdd = oddEven.isOdd(number)

if isOdd:
    print('Is odd number')
else:
    print('Is even number')