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
        print(key,value)         
    fd.close()
#d={}
#load_anag(d,'shortwords.txt')

def get_anag(d,chars):
    """ Return the list of anagrams of chars in d

    get_anag(dict(str,list(str)),str) => list(str)
    """
    return d.get(sort_string(chars),[])





        
