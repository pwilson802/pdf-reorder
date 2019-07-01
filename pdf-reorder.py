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
        if not pdf_file_check.match(file).group() == file:
            print('Check the files in the folder, one of them is not a pdf')
    except:
        print('Exception - Check the files in the folder, one of them is not a pdf')

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
    print(f"  {x['index']}: {x['filename']}  Pages: {x['pages']}") 


print(f'Please indicate what order the new pdf should be in:')
print('example: 1:1, 2:1, 1:1, 2:2, 1:1, 3:3')
input_test = re.compile(r'[\d:\d, ]+')
valid_pages = []
for i in range(len(pdf_objects)):
    valid_pages += [pdf_objects[i]['index'] + ':' + str(x) for x in range(1,pdf_objects[i]['pages']+1)]

# Adding all the below to try/except loop to catch if an incorrect page number has been added
while True:
    pages_valid = True
    page_layout = input('Enter the Pages: ')
    for page in page_layout.split(','):
        if page not in valid_pages:
            pages_valid = False
    if pages_valid == False:
        print('The Page {} is not a valid page number in your pdf files'.format(page))
        continue
    else:
        print('You have entered valid page numbers, processing...')
        break

pdf_writer = PyPDF2.PdfFileWriter()
output = open('c:\\temp\\pdf\\out.pdf', 'wb')

for page_index in page_layout.split(','):
    pdf, page = page_index.split(':')
    pdf_path = [x for x in pdf_objects if x['index'] == pdf][0]['fullpath']
    pdf_reader = PyPDF2.PdfFileReader(pdf_path)
    pdf_writer.addPage(pdf_reader.getPage(int(page)-1))


pdf_writer.write(output)
output.close()