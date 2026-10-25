'''
Objective 
Examine: 
• Source 
• Page index 
• Display page 
• Page label 
• Total pages 
'''

from pathlib import Path 
from langchain_community.document_loaders import (PyPDFLoader ) 
 
# ======================================== 
# SPECIFY PDF FILE 
# ======================================== 
pdf_path = ( Path(__file__).resolve().parent / "library_notice_three_pages.pdf") 

# ======================================== 
# CREATE PDF LOADER 
# ======================================== 
loader = PyPDFLoader( file_path=str(pdf_path), mode="page" ) 
 
# ======================================== 
# LOAD DOCUMENTS 
# ======================================== 
documents = loader.load() 
# ======================================== 
# DISPLAY PDF SUMMARY 
# ======================================== 
print("PDF METADATA REPORT") 
print("===================") 
print( "Total Documents:", len(documents) ) 

# ======================================== 
# DISPLAY METADATA FOR EACH PAGE 
# ======================================== 
for document in documents: 
    metadata = document.metadata 
    print("\nPAGE METADATA") 
    print("-------------") 
    print("Source:", Path(metadata["source"]).name) 
    print("Page Index:", metadata["page"] ) 
    print("Display Page:", metadata["page"] + 1 ) 
    print("Page Label:", metadata.get("page_label", "Not available" ) ) 
    print( "Total Pages:", metadata["total_pages"] ) 

