# Write your solution here
count = 0
sum = 0
pos=0
neg=0
print("Please type in integer numbers. Type in 0 to finish.")
while True:
    number = int(input("Number: "))
    count += 1
    sum += number
    if(number<0):
        neg+=1
    if(number>0):
        pos+=1
    if(number == 0):
        print("Numbers typed in ", count-1)
        print("The sum of the numbers is ", sum)
        mean = sum/(count-1)
        print("The mean of the numbers is " + str(mean))
        print("Positive numbers ", pos)
        print("Negative numbers ", neg)
        break
