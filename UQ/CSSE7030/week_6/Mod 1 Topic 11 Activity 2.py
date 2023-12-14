def enter_student_num() :
    """ Requests the user to input a UQ student number. Uses exception handling
    to print a message if the user did not input a valid number. Prints a message
    if the number is not in the correct form for a student number.
    """
    number = input("Enter a UQ student number: ")
    try :
        value = int(number)
    except ValueError:
        print("{0} is not a number".format(number))
        return
    if len(number) != 8:
        print("{0} is not in the correct form for a student number".format(number))
