try:
    a = 9
    b = 3
    print(a / b)
except ZeroDivisionError:
    print("Divide by zero")
else:
    print("No error")
finally:
    print("Program termnates")