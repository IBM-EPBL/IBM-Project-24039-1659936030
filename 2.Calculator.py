#program for calculator

#function for addition
def add(a,b):
    return a+b

#function for subtraction
def sub(a,b):
    return a-b

#function for multiplication
def mul(a,b):
    return a*b

#function for division
def div(a,b):
    return a/b

#function for modulus
def mod(a,b):
    return a%b

#function for power
def pow(a,b):
    return a**b

#function for floor division
def floordiv(a,b):
    return a//b

#function for calculator
def calculator():
    choice = input("Enter the operation you want to perform: ")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    if choice == "add":
        print(add(a,b))
    elif choice == "sub":
        print(sub(a,b))
    elif choice == "mul":
        print(mul(a,b))
    elif choice == "div":
        print(div(a,b))
    elif choice == "mod":
        print(mod(a,b))
    elif choice == "pow":
        print(pow(a,b))
    elif choice == "floordiv":
        print(floordiv(a,b))
    else:
        print("Invalid choice")

calculator()