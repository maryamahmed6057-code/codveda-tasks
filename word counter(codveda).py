try:
    filename= input("enter file name:")

    with open("text.txt","r") as file:
        text = file.read()

    word=text.split()
    print("number of words is",len(word))

except FileNotFoundError:
    print("file not found")


