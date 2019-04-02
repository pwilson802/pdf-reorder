# PDF Re-order - changes the order or pages in one or multiple pdf files
import os
import PyPDF2

pdf1file = open('c:\\temp\\cards\\dinos.pdf', 'rb')
pdf2file = open('c:\\temp\\cards\\back.pdf', 'rb')
pdf1Reader = PyPDF2.PdfFileReader(pdf1file)
pdf2Reader = PyPDF2.PdfFileReader(pdf2file)
pdfWriter = PyPDF2.PdfFileWriter()

singleinsert = pdf2Reader.getPage(0)

for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
    pdfWriter.addPage(singleinsert)

pdfOutputFile = open('c:\\temp\\cards\\dinofull.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1file.close()
pdf2file.close()
