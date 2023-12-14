def general_function(arg1, arg2, **kwargs):
    result = arg1 + arg2

    for key, value in kwargs.items():
        result += value

    return result
