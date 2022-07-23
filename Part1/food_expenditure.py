# Write your solution here
number1=int(input("How many times a week do you eat at the student cafeteria?"))
number2=float(input("The price of a typical student lunch?"))
number3=float(input("How much money do you spend on groceries in a week?"))
print("Average food expenditure:")
daily=float((number3+number2*number1)/7)
weekly=float((number3+number1*number2))
print(f"Daily: {daily} euros")
print(f"Weekly: {weekly} euros")

