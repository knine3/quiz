import PyPDF2

pdfObj = open('Transmission.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfObj)

print(pdfReader.numPages)



