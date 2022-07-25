# Write your solution here
number=float(input("Please type in a number: "))
print("Integer part: ", int(number))
if(type(number)==float):
    print("Decimal part: ", number-int(number))