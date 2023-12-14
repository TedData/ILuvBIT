#for i in range(4):
#    print(i)
    
for c in 'string':
    print(c)

for c in enumerate('string'):
    print(c)

for i,c in enumerate('string'):
    print(i,c)
    
def get_index(char, string):
    """Return the index of the first char in string.
    If not there return -1

    Parameters:
        char(str): the character being searched for
        string(str): the string being searched

    Return:
        int: the index where char first appears in string
    """
    for i, c in enumerate(string):
        if c == char:
            return i
    return -1

def get_all_indexes(char, string):
    """Return a tuple of all the indexes of char in string

    Parameters:
        char(str): the character being searched for
        string(str): the string being searched

    Return:
        tuple: the collection of indeces where char appears in string
    """
    result = ()
    for i, c in enumerate(string):
        if c == char:
            result += (i,) # result = result+(i,)
    return result

    
