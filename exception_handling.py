class CustomError(Exception):
    pass


try:
    f = int(input("Enter the Number"))
    a = 10
    b = -1
    if b < 0:
        raise CustomError("Custom Error")
    b = a // 0
    print(b)
    print("Hello this is the Program to Print the Ans")
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
except CustomError as c:
    print(c)
except Exception as e:
    print(e)

