def is_present(char, string):
    """Checks if a character is present in a string"""
    
    if len(string) == 0:
        # no more characters left in string to check,
        # therefore character is not in string
        return False

    if string[0] == char:
        return True

    return is_present(char, string[1:])
