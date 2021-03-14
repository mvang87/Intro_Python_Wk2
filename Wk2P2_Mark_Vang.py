"""
Program Name: Wk2P2_Mark_Vang
Student Name: Mark Vang
Course: ENTD200 D001 Winter 2021
Instructor: Professor Nigatu
Date: 3/14/2021
Copy Wrong: This is my work
"""

low = int(input("Please enter your Lower range: "))
high = int(input("Please enter your Higher range: "))
x = int(input("Please enter your first number: "))
y = int(input("Please enter your second number: "))

add = x + y
sub = x - y
product = x * y

def total():
    while True:
        if y != 0:
            print("You have selected a range of ", low, "to", high)
            print("The result of ", x, "+", y, "=", add)
            print("The result of ", x, "-", y, "=", sub)
            print("The result of ", x, "*", y, "=", product)
            print("The result of ", x, "/", y, "=", x / y)
            print("\nThank you for using my calculator!")
            break
        else:
            print("You have selected a range of ", low, "to", high)
            print("The result of ", x, "+", y, "=", add)
            print("The result of ", x, "-", y, "=", sub)
            print("The result of ", x, "*", y, "=", product)
            print("The result of ", x, "/", y, "=", x," You cannot divide by Zero.")
            print("\nThank you for using my calculator!")
            break

for i in low, high:
    if x < low:
        print("The input values are outside the input ranges. "
            "\nPlease check the numbers and try again"
            "\nThank you for using my calculator")
        break
    elif y < low:
        print("The input values are outside the input ranges. "
            "\nPlease check the numbers and try again"
            "\nThank you for using my calculator")
        break
    elif x > high:
        print("The input values are outside the input ranges. "
            "\nPlease check the numbers and try again"
            "\nThank you for using my calculator")
        break
    elif y > high:
        print("The input values are outside the input ranges. "
            "\nPlease check the numbers and try again"
            "\nThank you for using my calculator")
        break
    else:
        total()
        break

input("Press Enter to exit.")



