import os
import PyPDF2
import re

def get_pdf_info(pdf_files, folder):
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
    return pdf_objects

def reorder_pdf(pdf_objects, page_layout, output_file):
    output = open(output_file, 'wb')
    try:
        pdf_writer = PyPDF2.PdfFileWriter()

        for page_index in page_layout.split(','):
            pdf, page = page_index.split(':')
            pdf_path = [x for x in pdf_objects if x['index'] == pdf][0]['fullpath']
            pdf_reader = PyPDF2.PdfFileReader(pdf_path)
            pdf_writer.addPage(pdf_reader.getPage(int(page)-1))

        pdf_writer.write(output)
        output.close()
        return 'sucess'
    except Exception as e:
        return e