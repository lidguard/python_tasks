import os

#present options
def menu():
    print("What would you like to do?")
    option = input("""
    Press 1 to make a calculation
    Press 2 to read your calculations from calculator.txt
    Press 3 to quit 
    """)
    if option == "1":
        calculator()
    elif option == "2":
        readcalc()
    else:
        print("Goodbye!")
        exit()

#build the calulator
def calculator():
    file = open("calculator.txt", "a")
    try:
        number1 = int(input("Enter your first number: "))
    except ValueError:
        print("That's not a number! You'll have to start again.")
        exit()

    try:
        number2 = int(input("Enter your second number: "))
    except ValueError:
        print("That's not a number! You'll have to start again.")
        exit()

    operand = input("What would you like to do with these numbers? (+, -, /, *) ")

    if operand == "+":
        solution = number1 + number2
        print(f"{number1} {operand} {number2} = {solution}")
        file.write(f"{number1} {operand} {number2} = {solution}")

    elif operand == "-":
        solution = number1 - number2
        print(f"{number1} {operand} {number2} = {solution}")
        file.write(f"{number1} {operand} {number2} = {solution}")

    elif operand == "/":
        try:
            solution = number1 / number2
        except ZeroDivisionError:
            print("You cannot divide by 0 ")
        finally:
            print(f"{number1} {operand} {number2} = {solution}")
            file.write(f"{number1} {operand} {number2} = {solution}")


    elif operand == "*":
        solution = number1 * number2
        print(f"{number1} {operand} {number2} = {solution}")
        file.write(f"{number1} {operand} {number2} = {solution}")
    else:
        print("That's not a valid option, please start again")
        exit()

    again()


#to run the calculator again
def again():
    again = input("Do you want to run another calculation? (y/n) ")
    if again == "y":
        calculator()
    else:
        read = input("Would you like to see your calculations? (y/n) ")
        if read == "y":
            readcalc()
        else:
            print("Goodbye!")
            exit()

#to read the calculations
def readcalc():
    file = None
    file = input("Enter the file name: ")
    if os.path.exists(file):
        # open the file
        with open(file, "r") as f:
            data = f.read()
            print(f"""
            Here are your calculations:
            {data}""")
            again()
    else:
        print("File not found")








menu()

