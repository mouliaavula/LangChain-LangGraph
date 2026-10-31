from pathlib import Path
from reportlab.pdfgen import canvas
from pypdf import PdfReader

from langchain_core.documents import Document

#==========================================================
# Prepare Sample Pdf
#==========================================================
pdf_path = 'library_notice.pdf'

# Create canvas object to generate pdf file
pdf = canvas.Canvas(pdf_path)

pdf.drawString(60,750, 'LIBRARY NOTICE')
pdf.drawString(60,720, 'Library opens at 9 am every day.')
pdf.drawString(60,690, 'Library close at 6 pm every day.')
pdf.save()
#==========================================================
# Read pdf
#==========================================================
reader = PdfReader(pdf_path)

#==========================================================
# Create Langchain document
#==========================================================
page = reader.pages[0]

document  = Document(
    page_content = page.extract_text() or "",
    metadata={
        'source':pdf_path,
        'source_type':'pdf',
        'page':0,
        'total_pages':len(reader.pages)
    }
)

#==========================================================
# Display results
#==========================================================

print("Total pdf pages :",len(reader.pages))
print("Document type:",type(document).__name__)
print("\n Page content:")
print(document.page_content)
print("\nPage index :", document.metadata['page'])
print("source:", document.metadata['source'])


'''
Note:
The drawString() method takes 3 arguments.
Argument	Meaning	Explanation
60	X-coordinate	Distance from the left side of the PDF page
750	Y-coordinate	Distance from the bottom of the PDF page
heading	Text	Text to display at the given position

Remember: In ReportLab, 72 points = 1 inch.

'''
