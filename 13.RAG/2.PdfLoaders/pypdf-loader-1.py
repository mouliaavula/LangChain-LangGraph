'''
Objective : Load a single-page PDF and access: 
• Content 
• Source 
• Page index 
• Total pages 
• Metadata
'''
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

#=============================================================================
# Specify pdf file path
#=============================================================================

pdf_path = Path(__file__).resolve().parent/'library_notice.pdf'


#=============================================================================
# Create PDF loader
#=============================================================================

pdf_loader = PyPDFLoader(file_path=str(pdf_path))

#=============================================================================
# Load pdf document
#=============================================================================
documents = pdf_loader.load()

#=============================================================================
# Display return information
#=============================================================================

print("\n return type:", type(documents).__name__)
print("\n total documents:", len(documents))


#=============================================================================
# Access first document
#=============================================================================

document = documents[0]

#=============================================================================
# Display extracted content
#=============================================================================

print("\n Extracted page content=================================")
print(document.page_content)

#=============================================================================
# Display metadata
#=============================================================================
print("\n metadata=================================")
print(document.metadata)

#=============================================================================
# Display source information
#=============================================================================
print("\n metadata source info=================================")
print(document.metadata['source'])

#=============================================================================
# Display page information
#=============================================================================
print("\n metadata page info=================================")
print(document.metadata['page'])

print("\n metadata total pages=================================")
print(document.metadata['total_pages'])

