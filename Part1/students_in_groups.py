students = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))
formed=students//group_size
if(students%group_size!=0):
    print("Number of groups formed:", formed + 1)
else:
     print("Number of groups formed:", students // group_size)