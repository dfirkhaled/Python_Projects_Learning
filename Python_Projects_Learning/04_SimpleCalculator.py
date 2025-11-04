# Small Calc Project
# Created by khaled in 2025/31/10 at 5:15 PM


while True:
    Num1 = float(input("Inter your first number (Must be number not string or ....): "))
    Operator = input("Inter Your Operator like (+/*/....) (type: help, to see all operators): ")


    if Operator == "help" or Operator == "Help":
        print("All Arthimetic operators is: (+,-,*,/,//,%,**)")
        print("=" * 70)
        continue
    

    elif Operator == "-":
        Num2 = float(input("Inter your second number (Must be number not string or ....): "))
        Sum = Num1 - Num2
        print("=" * 70)
        print(f"Your First Number is: {Num1}")
        print(f"Your Operator is: {Operator}")
        print(f"Your Second Number is: {Num2}")
        print("=" * 70)
        print(f"Your Sum is: {Sum}")
        print("=" * 70)

    elif Operator == "*":
        Num2 = float(input("Inter your second number (Must be number not string or ....): "))
        Sum = Num1 * Num2
        print("=" * 70)
        print(f"Your First Number is: {Num1}")
        print(f"Your Operator is: {Operator}")
        print(f"Your Second Number is: {Num2}")
        print("=" * 70)
        print(f"Your Sum is: {Sum}")
        print("=" * 70)

    elif Operator == "/":
        Num2 = float(input("Inter your second number (Must be number not string or ....): "))
        if Num2 == 0:
            print("Can't Division By zero :(")
            continue
        Sum = Num1 / Num2
        print("=" * 70)
        print(f"Your First Number is: {Num1}")
        print(f"Your Operator is: {Operator}")
        print(f"Your Second Number is: {Num2}")
        print("=" * 70)
        print(f"Your Sum is: {Sum}")
        print("=" * 70)

    elif Operator == "//":
        Num2 = float(input("Inter your second number (Must be number not string or ....): "))
        Sum = Num1 // Num2
        print("=" * 70)
        print(f"Your First Number is: {Num1}")
        print(f"Your Operator is: {Operator}")
        print(f"Your Second Number is: {Num2}")
        print("=" * 70)
        print(f"Your Sum is: {Sum}")
        print("=" * 70)

    elif Operator == "%":
        Num2 = float(input("Inter your second number (Must be number not string or ....): "))
        Sum = Num1 % Num2
        print("=" * 70)
        print(f"Your First Number is: {Num1}")
        print(f"Your Operator is: {Operator}")
        print(f"Your Second Number is: {Num2}")
        print("=" * 70)
        print(f"Your Sum is: {Sum}")
        print("=" * 70)

    elif Operator == "**":
        Num2 = float(input("Inter your second number (Must be number not string or ....): "))
        Sum = Num1 ** Num2
        print("=" * 70)
        print(f"Your First Number is: {Num1}")
        print(f"Your Operator is: {Operator}")
        print(f"Your Second Number is: {Num2}")
        print("=" * 70)
        print(f"Your Sum is: {Sum}")
        print("=" * 70)
    

    elif Operator == "+":
        Num2 = float(input("Inter your second number (Must be number not string or ....): "))
        Sum = Num1 + Num2
        print("=" * 70)
        print(f"Your First Number is: {Num1}")
        print(f"Your Operator is: {Operator}")
        print(f"Your Second Number is: {Num2}")
        print("=" * 70)
        print(f"Your Sum is: {Sum}")
        print("=" * 70)

    else:
        print("Not defined operator try again:)")
    

    again = input("Do you want to calculate again? (y/n): ")
    if again.lower() != "y":
        print("Exiting calculator... Goodbye!")
        break