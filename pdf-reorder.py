# PDF Re-order - changes the order or pages in one or multiple pdf files
# TODO
# Add page checker to pdf file to check user input is valid for the pages
# Make into a flask app

import os
import PyPDF2
import re
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('folder', help='The folder containing the pdf files')
args = parser.parse_args()
folder = args.folder

# Reading the pdf files and checking they all have a valid name before processing them
pdf_files = os.listdir(folder)
pdf_file_check = re.compile(r'.+[.]pdf')
for file in pdf_files:
    try:
        if not re.match(file_check, file).group == file:
            print('Check the files in the folder, one of them is not a pdf')
    except:
        print('Check the files in the folder, one of them is not a pdf')

# Making a dict of all the pdf files so they can be accessed easily later
pdf_objects = []
for num,filename in enumerate(pdf_files):
    pdf_details = {}
    pdf_path = os.path.join(folder, filename) 
    with open(pdf_path, 'rb') as pdffile:
        pdfreader = PyPDF2.PdfFileReader(pdffile)
        pdf_details['filename'] = filename
        pdf_details['fullpath'] =  pdf_path
        pdf_details['index'] = str(num+1)
        pdf_details['pages'] = pdfreader.getNumPages()
        pdf_objects.append(pdf_details)

print(pdf_objects)
print(f'{len(pdf_files)} PDF files are loaded, there are in this order:')
for x in pdf_objects:
    print(f"  {x['index']}: {x['filename']}") 



print(f'Please indicate what order the new pdf should be in:')
print('example: 1:1, 2:1, 1:1, 2:2, 1:1, 3:3')
input_test = re.compile(r'[\d:\d, ]+')
while True:
    page_layout = input('Enter the Pages: ')
    if not re.match(input_test, page_layout).group() == page_layout:
        print('Please enter the pages as valid input')
        print('example: 1:1, 2:1, 1:1, 2:2, 1:1')
    else:
        print('Good, the new pdf will now be created.')
        break

pdfWriter = PyPDF2.PdfFileWriter()
for page_index in page_layout.split(','):
    pdf, page = page_index.split(':')
    # print(pdf_objects)
    # print([x for x in pdf_objects if x['index'] == pdf])
    pdf_path = [x for x in pdf_objects if x['index'] == pdf][0]['fullpath']
    with open(pdf_path, 'rb') as pdffile:
        pdfreader = PyPDF2.PdfFileReader(pdffile)
        pageObj = pdfreader.getPage(int(page))
        pdfWriter.addPage(pageObj)


pdfOutputFile = open('c:\\temp\\pdf\\out.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()


"""
for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
    pdfWriter.addPage(singleinsert)

pdfOutputFile = open('c:\\temp\\cards\\dinofull.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1file.close()
pdf2file.close()
"""