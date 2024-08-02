from PyPDF2 import PdfReader, PdfWriter

# Create a PdfReader object for the input PDF
reader = PdfReader('WAD_UNIT-4_PHP_Notes.pdf')

# Create a PdfWriter object for the output PDF
writer = PdfWriter()

# Loop through all pages in the reader
for page in reader.pages:
    # Add each page to the writer
    writer.add_page(page)

# Encrypt the PDF with a password
writer.encrypt('Password')

# Write the encrypted PDF to a new file
with open('encrypted_WAD_UNIT-4_PHP_Notes.pdf', 'wb') as file:
    writer.write(file)

print('PDF encrypted')
