
from docx import Document

document = Document()
terms = []

path = input("What is the file path?")
readFile = open(path, "r")
Lines = readFile.readlines()


userInput = input("What section would you like to find? (enter exact name) ")
searchTerm = userInput.upper()    #Removed upper(), for searching content based on case sensitivity.
terms.append(searchTerm)

proceed = 0

while proceed == 0:
    moreYesNo = input("Is there another section you would like to find? (Y/N) ")
    if moreYesNo.upper() == "Y":
        extraTerm = input("Please enter a specific section name: ")
        extraTermUpper = extraTerm
        terms.append(extraTermUpper)
    elif moreYesNo.upper() == "N":
        proceed = 1



for term in terms:       # Here I use a for loop, which will traverse the entire text, 
    termLineNo = []         #find all the content in the terms, and write it into the document.

    lineNo = 0

    for line in Lines:
        if term in line:
            termLineNo.append(lineNo)     # record the line number where search term is
        lineNo += 1

    for i in termLineNo:
        termLineNo = i
        lineEmpty = 0

        while lineEmpty == 0:   # while the line is not empty
            if Lines[termLineNo] != "\n":
                p1 = document.add_paragraph(Lines[termLineNo])
                termLineNo += 1
            else:
                lineEmpty = 1

    print("Finished searching for", term)

print("Finished writing Word document.")
document.save("cartesian.docx")
readFile.close()




