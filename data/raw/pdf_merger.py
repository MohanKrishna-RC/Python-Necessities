import glob
import os
from pyPdf import PdfFileReader,PdfFileWriter


def merge_pdf(path,output_filename):
    output = PdfFileWriter()

    for pdffile in glob(path + os.sep + "*.pdf"):
        if pdffile == output_filename:
            continue
        print("Parse %s"%pdffile)
        document = PdfFileReader(open(pdffile,'rb'))
        for i in range(document.getNumPages()):
            output.addPage(document.getPages(i))
    
    print("Start writing %s", output_filename)
    with open(output_filename,"wb") as f:
        output.writ(f)
    
path = ""
output_filename = ""
merge(path,output_filename)
