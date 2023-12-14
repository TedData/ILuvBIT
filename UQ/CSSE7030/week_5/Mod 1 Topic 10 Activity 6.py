def sort_string(word):
    """ Return the sorted string corresponding to word

    ...
    """
    chars=sorted(word)
    return ''.join(chars)

def load_anag(d,filename):
    """ Add anagrams from filename to the dictionary, d

    ...
    """
    fd=open(filename, 'r')
    for line in fd:
        word=line.strip()
        key=sort_string(word)
        value=d.get(key)
        if value is None:
            value=[word]
            d[key]=value
        elif word not in value:
            value.append(word)        
    fd.close()

def remove_words(d):
    """ Loops through a dictionary (where key is an alphabetically
    sorted string, and value is a list of anagrams), and
    copies entries in the dictionary over to a new dictionary if there
    is more than one word in the anagram list.
    
    Returns a new dictionary that does not include words that
    have no anagrams.
    """
    
    new_dict = {}
    for key, value in d.items():
        if len(value) > 1:
            new_dict[key] = value
    return new_dict
   

d={}
load_anag(d,'shortwords.txt')
dictionary = remove_words(d)
print(dictionary)



        
