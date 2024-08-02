from pdf2docx import Converter
pdf_file='PHP programs.pdf'
docx_file='PHP programs.docx'
cv=Converter(pdf_file)
cv.convert(docx_file)
cv.close()
