user_input = float(input("Enter a nummber: "))

if (user_input > 100) and (user_input % 2 == 0):
    print("Bigger and even")
elif user_input > 100:
    print("Bigger")
elif user_input <= 100 and (user_input % 2 == 0):
    print("Smaller and even")
else:
    print("Smaller")


