try:
    a = int(input("First number: "))
    b = int(input("Second number: "))
    r = a / b

except (ValueError, TypeError):
    print("We had a problem with the type of data that you typed.")

except ZeroDivisionError:
    print("You can't divide a number by zero.")

except KeyboardInterrupt:
    print("The user cancelled the program.")

except Exception as error:
    print(f"The error occurred: {error}")

else:
    print(f"Dividing {a} by {b}, we have {r}")
