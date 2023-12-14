import urllib.request
staffURL = 'file:///C:/Users/uqposhe1/Downloads/Times%20and%20rooms%20%E2%80%93%20CSSE1001S_6860_60605.html'

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

""" Below is the code to scrape the names of the TUTORS from the 2018 CSSE1001/7030 web-site
The code relies on first finding the phrase "TUTORS", then finding a start of paragraph tag
(i.e a <p>) and then finally an end of paragraph tag (i.e. </p>).
The HTML source code in the vicinity of the phrase "TUTORS" is shown below:

<p>TUTORS</p> 
 <p>Anna Truffet, Ashleigh Richardson, Benjamin Martin, Brae Webb, Harry Keightly, Henry O'Brien, Joshua Arnold, Mike Pham, Rudi&nbsp;Scarpa, Steven Summers, Wilson Kong, Samuel Eadie, Luis Woodrow, Justin Luong</p> 
 <br>
"""

text = getURL()
heading_index = find("TUTORS", text, 0)
if heading_index is None:
    print("Heading not found")
else:
    new_paragraph_index = find("<p>", text, heading_index)
    if new_paragraph_index is None:
        print("New paragraph not found")
    else:
        end_of_paragraph_index = find("</p>", text, new_paragraph_index)
        if end_of_paragraph_index is None:
            print("tag not found")
        else:
            print(text[new_paragraph_index+3:end_of_paragraph_index])

def getText():
    fd = open('staff.html', 'r')
    text = fd.read()
    fd.close()
    return text
