correct_pin = "2006"
attempts = 0

while attempts < 3:
    pin = input("PIN: ")

    if pin == correct_pin:
        print("Access granted")
        break
    else:
        attempts = attempts + 1

        if attempts == 3:
            print("Card blocked")
        else:
            print("Incorrect PIN")