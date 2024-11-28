number = int(input("Enter a number: "))

if number > 0:
    if number % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")

elif number < 0:
    if abs(number) > 10:
        print("Large Negative")
    else:
        print("Small Negative")

else:
    print("Zero")