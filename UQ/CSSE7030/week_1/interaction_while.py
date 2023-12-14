name = input("What is your name? ")
if name == "Tim" :
    print("Greetings, Tim the Enchanter")
elif name == "Brian" :
    print("Bad luck, Brian")
else :
    print("Hello " + name + ".")

topic = input("What do you want to talk about? ")
while topic != "nothing" :
    like = input("Do you like " + topic + "? ")
    response = input("Why do you think that? ")
    print("I also think that", response)
    topic = input("What do you want to talk about? ")

print("Okay. Goodbye, " + name + "!")
