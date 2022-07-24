# Write your solution here
name = input("Please tell me your name: ")
if(name == "Jerry"):
    print("Next please!")
if(name != "Jerry"):
    howManyPortions = int(input("How many portions of soup? "))
    portionPrice = 5.90*howManyPortions
    print(f"The total cost is {portionPrice}")
    print("Next please!")
