# PDF Re-order - changes the order or pages in one or multiple pdf files
# TODO
# Add page checker to pdf file to check user input is valid for the pages
# Make into a flask app
import os
import PyPDF2
import re
import argparse
from apps import pdf_tools

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
pdf_objects = pdf_tools.get_pdf_info(pdf_files, folder)

print(pdf_objects)
print(f'{len(pdf_files)} PDF files are loaded, there are in this order:')
for x in pdf_objects:
    print(f"  {x['index']}: {x['filename']}  Pages: {x['pages']}") 

print(f'Please indicate what order the new pdf should be in:')
print('example: 1:1, 2:1, 1:1, 2:2, 1:1, 3:3')
valid_pages = []
for i in range(len(pdf_objects)):
    valid_pages += [pdf_objects[i]['index'] + ':' + str(x) for x in range(1,pdf_objects[i]['pages']+1)]

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

output_file = 'c:\\temp\\pdf\\out.pdf'

pdf_reorder = pdf_tools.reorder_pdf(pdf_objects, page_layout, output_file)

if pdf_reorder == 'success':
    print(f'Your new pdf file has been saved as {output_file}')
else:
    print('The pdf file re-order failed with error:')
    print(pdf_reorder)