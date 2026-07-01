import math
import random
from datetime import datetime

history = {}

while True:
    print("\n1.Basic Arithmetic")
    print("2.Scientific Calculation")
    print("3.Generate Random Number")
    print("4.View History")
    print("5.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Enter operator (+,-,*,/): ")

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            result = a / b
        else:
            print("Invalid operator")
            continue

        print("Result:", result)
        history[str(datetime.now())] = result

    elif choice == "2":
        num = float(input("Enter number: "))
        result = math.sqrt(num)
        print("Square Root:", result)
        history[str(datetime.now())] = result

    elif choice == "3":
        result = random.randint(1, 100)
        print("Random Number:", result)
        history[str(datetime.now())] = result

    elif choice == "4":
        for time, value in history.items():
            print(time, ":", value)

    elif choice == "5":
        break

    else:
        print("Invalid choice")