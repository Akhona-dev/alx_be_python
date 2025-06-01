numb1 = int(input("Enter the first number:"))
numb2 = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):.")

match operation:
    case "+":
        result = numb1 + numb2
        print(f"The result is{result}")
    case "-":
        result = numb1 - numb2
        print(f"The result is{result}")
    case "*":
        result = numb1 * numb2
        print(f"The result is{result}")
    case "/":
        if numb2 == 0:
            print("cannot divide by zero")
        else:
            result = numb1 / numb2
            print(f"The result is {result}")
    case _:
        print(f"invalid operation")