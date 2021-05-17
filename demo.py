# import packages
import PyPDF2
import re

# open the pdf file
object = PyPDF2.PdfFileReader("leph101.pdf")

# get number of pages
NumPages = object.getNumPages()

# define keyterms
String = "one"
# extract text and do the search
for i in range(0, 4):#NumPages
    PageObj = object.getPage(i)
    Text = PageObj.extractText() 
    ResSearch = re.search(String, Text)
    if ResSearch != None:
        print("'"+String+"' exists in page : ",i)