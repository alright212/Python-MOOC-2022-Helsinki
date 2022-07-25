pin = "4321"

attempts = 0

while True:
    user_pin = input("PIN: ")
    attempts += 1

    if user_pin == pin:
        if attempts == 1:
            print("Correct! It only took you one single attempt!")
        else:
            print(f"Correct! It took you {attempts} attempts")
        break
    else:
        print("Wrong")