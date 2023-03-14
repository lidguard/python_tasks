'''Write a function named 'format_number' that takes a
non-negative number as its only parameter. Your function
should convert the number to a string and add commas as a
thousand separators. For example, calling format_number(1000000)
should return "1,000,000".'''

#using input to get numbers rather than hard coding one into the function so that it can be rerun over and over until the user is bored


def format_number():
    #try/except to allow for non-int input error handling
    try:
        #take input as integer to convert into string with formatting later
        number = int(input("Enter a number to format in thousands: "))
        #if statement to allow error handling
        if number >= 1000:
            #string formatting number with commas
            f_num = ("{:,}".format(number))
            print(f"Your number formatted into thousands is: {f_num}")

        #else statement corrects user to expected input and try again
        else:
            print("Error: your number must be greater than 999. Please try again.\n")
            format_number()
            
    #except corrects non-integer input and requests corrected input
    except ValueError:
        print("Error: not a number. Please try again. \n")
        format_number()


format_number()
