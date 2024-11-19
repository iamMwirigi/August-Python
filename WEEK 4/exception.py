a = 5
b = 0

# print(a/b)

try:
    print(a/b)
    k = int(input("Enter a number: "))

except ZeroDivisionError as e:
    print("You can't divide by zero", e)
except ValueError as e:
    print("You can't divide by zero", e)
except Exception as e:
    print("You can't divide by zero", e)
finally:
    print("You gat this bro")