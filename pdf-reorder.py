# PDF Re-order - changes the order or pages in one or multiple pdf files
import os
import PyPDF2
import re
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('folder', help='The folder containing the pdf files')
args = parser.parse_args()
folder = args.folder

print(os.listdir(folder))
pdf1file = open('c:\\temp\\cards\\dinos.pdf', 'rb')
pdf2file = open('c:\\temp\\cards\\back.pdf', 'rb')
pdf1Reader = PyPDF2.PdfFileReader(pdf1file)
pdf2Reader = PyPDF2.PdfFileReader(pdf2file)
pdfWriter = PyPDF2.PdfFileWriter()

singleinsert = pdf2Reader.getPage(0)

print('2 PDF Files are loaded, please indicate what order the new pdf should be in:')
print('example: 1:1, 2:1, 1:1, 2:2, 1:1')
input_test = re.compile(r'[\d:\d, ]+')
while True:
    page_layout = input('Enter the Pages: ')
    if not re.match(input_test, page_layout).group() == page_layout:
        print('Please enter the pages as valid input')
        print('example: 1:1, 2:1, 1:1, 2:2, 1:1')



for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
    pdfWriter.addPage(singleinsert)

pdfOutputFile = open('c:\\temp\\cards\\dinofull.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1file.close()
pdf2file.close()
