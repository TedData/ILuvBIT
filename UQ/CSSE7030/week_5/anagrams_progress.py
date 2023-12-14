def load_anagrams(filename):
    """
    Load anagrams from 'filename'

    Parameters:
        filename (str): The name of the words file

    Return:
        dict<str: str>
    """

    file = open(filename, 'r')
    anagrams = {}

    for line in file:
        word = line.strip()

        key = get_anagram_key(word)

        if key not in anagrams:
            anagrams[key] = []

        anagrams[key].append(word)

    file.close()

    return anagrams

def get_anagram_key(word):
    """Converts word to its unique anagram key

    ..."""

    return "".join(sorted(word))

def get_anagrams(anagrams, word):
    key = get_anagram_key(word)
    return anagrams[key]
    

short_anagrams = load_anagrams("shortwords.txt")
full_anagrams = load_anagrams("words.txt")

print(get_anagrams(full_anagrams, "eats"))

