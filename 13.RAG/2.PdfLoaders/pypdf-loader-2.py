'''
Objective :Load a three-page PDF and access each page separately. 
'''
from pathlib import Path
from shlex import join
from langchain_community.document_loaders import PyPDFLoader

#=======================================================================================
# Specify PDF file
#=======================================================================================
pdf_file = Path(__file__).resolve().parent /'library_notice_three_pages.pdf'

#=======================================================================================
# Create page wise pdf loader
#=======================================================================================

pdf_loader = PyPDFLoader(file_path=str(pdf_file),mode='page')

#=======================================================================================
# Load pdf pages
#=======================================================================================

documents = pdf_loader.load()

#=======================================================================================
# Display total documents
#=======================================================================================

print("\n Total documents:",len(documents))

#=======================================================================================
# Display each page
#=======================================================================================

for document in documents:
    page_index = document.metadata['page']
    page_number = page_index + 1
    text = " "+join(document.page_content.split())
    print("\n Page Number: ", page_number)
    print("\n Page content: ", text)


