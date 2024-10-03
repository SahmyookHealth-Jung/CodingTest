# 파이썬으로 만든 계산기

def puls (a, b):
    return a+b

def minus (a, b):
    return a-b

def multiply (a, b):
    return a*b

def divide (a, b):
    return a/b
    
print("원하는 계산 방법을 선택하세요.")

print("1. Addition (+)")

print("2. Subtraction (-)")

print("3. Multiplication (*)")

print("4. Division (/)")


while True:
    choice = int(input("Enter your choice: "))

    if choice == 1:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = puls(num1, num2)
        print(f"{num1} + {num2} = {result}")

    elif choice == 2:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = minus(num1, num2)
        print(f"{num1} - {num2} = {result}")

    elif choice == 3:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")

    elif choice == 4:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")

    else:
        print("Invalid choice. Please try again.")
        break

