import PyPDF2
import re
PDFFile = open("TOIM_2019_11_16.pdf",'rb')

PDF = PyPDF2.PdfFileReader(PDFFile)
pages = PDF.getNumPages()
key = '/Annots'
uri = '/URI'
ank = '/A'
urls = []

for page in range(pages):
    print("Current Page: {}".format(page))
    pageSliced = PDF.getPage(page)
    page_content = pageSliced.extractText()
    #extracting the urls from the texts using regex
    urls.append(re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', page_content.replace('\n', ' ')))
    urls.append(re.findall(r'\S+@\S+', page_content.replace('\n','')))
    
print(urls)