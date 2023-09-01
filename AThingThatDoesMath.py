import math

print("1 Addition")
print("2 Subtraction")
print("3 Multiplication")
print("4 Division")

choice = input("Enter your choice: ")

num1 = float(input("Enter number here: "))
num2 = float(input("Enter second number here: "))

if choice == "1":
    print(num1, "+", num2, "=", (num1+num2))

if choice == "2":
    print(num1, "-", num2, "=", (num1-num2))

if choice == "3":
    print(num1, "*", num2, "=", (num1*num2))

if choice == "4":
    print(num1, "/", num2, "=", (num1/num2))

