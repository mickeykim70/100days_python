# calculator

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Mutiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

# Exponential
def exponential(n1, n2):
    return n1 ** n2

# make dictionary with symbols and numbers
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": exponential,
    }
def calculator():
    num1 = float(input("What's the first number? "))

    for operator in operations:
        print(operator)
        
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operator: ")
        num2 = float(input("What's the next number? "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input("Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()
            
calculator()