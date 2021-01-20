"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# repeat forever:
#     read input
#     tokenize input
#         if the first token is "q":
#             quit
#         else:
#             (decide which math function to call based on first token)
#             if the first token is 'pow':
#                   call the power function with the other two tokens
#             (...etc.)
# +, -, /, *, **, %, **2, **3



while True:
    user_input = input("Enter your equation: ")
    if user_input == "q":
        print("You will exit now")
        break
    tokens = user_input.split(" ")
    operator = tokens[0]
    number1 = float(tokens[1])
    number2 = float(tokens[2])
    if len(tokens) < 2:
        print("Not enough inputs.")
        continue

    elif operator == "add":
        print(add(number1,number2))

    elif operator == "subtract":
        print(subtract(number1,number2))

    elif operator == "multiply":
        print(multiply(number1,number2))

    elif operator == "divide":
        print(divide(number1,number2))

    elif operator == "square":
        print(square(number1,number2))

    elif operator == "cube":
        print(cube(number1,number2))

    elif operator == "power":
        print(power(number1,number2))

    elif operator == "mod":
        print(mod(number1,number2))