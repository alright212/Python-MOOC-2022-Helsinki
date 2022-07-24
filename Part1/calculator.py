# Write your solution here
number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
operation = input("Operation: ")
if(operation == "add"):
    sum = number1+number2
    print(f"{number1} + {number2} = {sum}")
if(operation == "multiply"):
    multiply = number1*number2
    print(f"{number1} * {number2} = {multiply}")
if(operation == "subtract"):
    subtract = number1-number2
    print(f"{number1} - {number2} = {subtract}")
