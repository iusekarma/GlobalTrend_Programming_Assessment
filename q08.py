def operate(n1, n2, o):
    if o == '+':
        return n1 + n2
    elif o == '-':
        return n1 - n2
    elif o == '*':
        return n1 * n2
    elif o == '/':
        if n2 == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
        return n1 / n2
    else:
        return "Error: Invalid operator. Please only use one of '+', '-', '*', '/'."

if __name__ == "__main__":
    n1 = 10
    n2 = 5
    operators = ['+', '-', '*', '/']
    for o in operators:
        res = operate(n1, n2, o)
        print(f"{n1} {o} {n2} = {res}")