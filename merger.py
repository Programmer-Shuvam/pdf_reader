import PyPDF2
 
 
def PDFmerge(pdfs, output):
    # creating pdf file merger object
    pdfmerger = PyPDF2.PdfFileMerger()
 
    # appending pdfs one by one
    for pdf in pdfs:
        pdfmerger.append(pdf)
 
    # writing combined pdf to output pdf file
    with open(output, 'wb') as f:
        pdfmerger.write(f)
 
 
def main():
    # pdf files to merge
    pdfs = ['leph101.pdf', 'leph102.pdf']
 
    # output pdf file name
    output = 'ph.pdf'
 
    # calling pdf merge function
    PDFmerge(pdfs=pdfs, output=output)
 
 
if __name__ == "__main__":
    # calling the main function
    main()