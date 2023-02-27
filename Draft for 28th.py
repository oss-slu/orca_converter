from docx import Document

document = Document()

path = input("What is the file path?")
readFile = open(path, "r")
Lines = readFile.readlines()

terms = []

def start():
    userInput = input("What section would you like to find? (enter exact name) ")
    searchTerm = userInput.upper()
    terms.append(searchTerm)

    proceed = 0

    while proceed == 0:
        moreYesNo = input("Is there another section you would like to find? (Y/N) ")
        if moreYesNo == "Y":
            extraTerm = input("Please enter a specific section name: ")
            extraTermUpper = extraTerm.upper()
            terms.append(extraTermUpper)
        elif moreYesNo == "N":
            proceed = 1

def findTerms():
    
    for term in terms:
        lineNo = 0
        termLineNo = []
        lineEmpty =0
        for line in Lines:
            if term in line:
                termLineNo.append(lineNo)     # record the line number where search term is
            lineNo += 1

        for i in termLineNo:
            termLineNo = i
            lineEmpty = 0


            while lineEmpty == 0:
                if Lines[termLineNo] != "\n":
                    section = document.add_paragraph(Lines[termLineNo])
                    termLineNo += 1
                else:
                    lineEmpty = 1


def closeAndSave():
    document.save("data_conversion.docx")
    readFile.close()


def main():
    start()
    findTerms()
    closeAndSave()
    print(terms)


if __name__ == "__main__":
    main()
    
