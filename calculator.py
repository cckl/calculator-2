"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import add, subtract, multiply, divide, square, cube, mod, power 

# def count_tokens(tokens):
#     return len(tokens)


# Your code goes here
while True:
    arithmetic_operation = input(">")
    tokens = arithmetic_operation.split(" ")
    if tokens[0] == "q":
        break
    token_one = int(tokens[1])
    if len(tokens) > 2:
        token_two = int(tokens[2])
        if tokens[0] == "+":
            print(add(token_one, token_two))
        elif tokens[0] == "-":
            print(subtract(token_one, token_two))
        elif tokens[0] == "*":
            print(multiply(token_one, token_two))
        elif tokens[0] == "/":
            print(divide(token_one, token_two))
        elif tokens[0] == "mod":
            print(mod(token_one, token_two))
        elif tokens[0] == "pow":
            print(power(token_one, token_two))    
    elif tokens[0] == "square":
        print(square(token_one))
    elif tokens[0] == "cube":
        print(cube(token_one))
    





