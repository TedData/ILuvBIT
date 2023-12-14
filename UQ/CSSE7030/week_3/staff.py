import urllib.request
staffURL = 'file:///C:/Python34/Examples/Times%20and%20rooms%20%E2%80%93%20CSSE1001S_6860_60605.html'

def getURL():
    stream = urllib.request.urlopen(staffURL)
    text = stream.read().decode() # or text="".join( chr(x) for x in bytearray(fd) )
    stream.close()
    return text

def find(substr, string, start):
    """Return the position of the first substr in string starting from start.
    Return None if not found

    find(str, str, int) -> int
    """

    pos = start
    size = len(substr)
    while pos < len(string):
        if substr == string[pos:pos+size]:
            return pos
        pos += 1
    return None

text = getURL()
heading_index = find("practicals", text, 0)
if heading_index is None:
    print("Heading not found")
else:
    room_index = find("Room", text, heading_index)
    if room_index is None:
        print("Room not found")
    else:
        tag_index = find("<", text, room_index)
        if tag_index is None:
            print("tag not found")
        else:
            print(text[room_index:tag_index])

def getText():
    fd = open('staff.html', 'r')
    text = fd.read()
    fd.close()
    return text
