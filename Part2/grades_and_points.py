# Write your solution here
points=int(input("How many points [0-100]: "))

if(points>=0 and points<=49):
    print(f"Grade: fail")
elif(points>=50 and points<=59):
    print(f"Grade: 1")
elif(points>=60 and points<=69):
    print(f"Grade: 2")
elif(points>=70 and points<=79):
    print(f"Grade: 3")
elif(points>=80 and points<=89):
    print(f"Grade: 4")
elif(points>=90 and points<=100):
    print(f"Grade: 5")
else:
    print(f"Grade: impossible!")





