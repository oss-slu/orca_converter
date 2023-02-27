import docx


# Load the docx file
doc = docx.Document('/Users/samsam/Desktop/newdoc5.docx')


# Loop through each paragraph and search for keywords
start_keyword = input('Keyword1')
end_keyword = input('Keyword2')

# Initialize a flag to indicate whether we are currently between the start and end keywords
between_keywords = False

# Loop through each paragraph and print the text between the start and end keywords
for paragraph in doc.paragraphs:
    text = paragraph.text.lower()  # Convert paragraph text to lowercase
    if start_keyword.lower() in text:
        between_keywords = True
    elif end_keyword.lower() in text:
        between_keywords = False
    elif between_keywords:
        print(paragraph.text)
