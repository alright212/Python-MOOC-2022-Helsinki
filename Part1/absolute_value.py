# Write your solution here
number=int(input("Please type in a number:"))
if(number<0):
    absoluteValue=number*(-1)
    print(f"The absolute value of this number is {absoluteValue}")
if(number>0):
    print(f"The absolute value of this number is {number}")
if(number==0):
    print(f"The absolute value of this number is {number}")
