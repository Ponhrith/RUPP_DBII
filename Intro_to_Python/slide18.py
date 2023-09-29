try:
    result = 10/0
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero")
finally:
    print("This will always execute")