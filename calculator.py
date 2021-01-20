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
    tokens = user_input.split(" ")
    if user_input == "q":
        print("You will exit now")
        break
    elif len(tokens) < 2:
        print("Not enough inputs.")
        continue
    operator == tokens[0]
    number1 == tokens[1]
    number2 == tokens[2]
    # elif operator == "add":
    #     return add(number1,number2)



