def get_words(filename):
    """ Function that returns a list of
    all the words in the file that contain
    the letter z

    Parameters:
        filename: The name of the file to open

    Return:
        list: a list of all the words that contain z

    """

    fd = open(filename)
    result = []
    for line in fd:
        word = line.strip()
        if "z" in word:
            result.append(word)
    fd.close()
    return result
