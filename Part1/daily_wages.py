# Write your solution here
wageH=float(input("Hourly wage: "))
workedH=int(input("Hours worked: "))
day=input("Day of the week: ")
if(day=="Sunday"):
    wages=(2*wageH)*workedH
    print(f"Daily wages: {wages} euros")
else:
    wages=(wageH*workedH)
    print(f"Daily wages: {wages} euros")
