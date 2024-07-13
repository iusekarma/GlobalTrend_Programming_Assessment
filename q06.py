def divide(x, y):
    if y != 0:
        return x / y
    else:
        raise ZeroDivisionError("Error: Cannot divide by zero.")
    
if __name__ == "__main__":
    print(divide(2,2))
    print(divide(2,0))