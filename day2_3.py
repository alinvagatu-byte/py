def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num1 == 0:
        print('Division imposible')
    else:
        return num1 / num2
    

while True:
    print("\nMenu:")
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    choice = input("\nPlease choice an option: ")
    
    if choice == '5':
        print('Exiting...')
        break
    else:
        num1 = float(input("Please enter first number: "))
        num2 = float(input("Please enter second number: "))
        
        if choice == '1':
            print(f"Result is: {add(num1, num2)}")
        if choice == '2':
            print(f"Result is: {sub(num1, num2)}")
        if choice == '3':
            print(f"Result is: {multiply(num1, num2)}")
        if choice == '4':
            print(f"Result is: {divide(num1, num2)}")
            