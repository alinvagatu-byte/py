# Exercise prime number

num = int(input("add a number: "))

if num > 0:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prim number")
            break
    else:
        print(f"{num} is a prim number")
else:
    print(f"{num} is not a prime number")