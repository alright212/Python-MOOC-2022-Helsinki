 
password = input("Password: ")
repeat = input("Repeat password: ")
while repeat != password:
    print("They do not match!")
    repeat = input("Repeat password: ")
print("User account created!")
