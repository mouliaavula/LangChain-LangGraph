'''
Objective :Process PDF pages one by one and identify pages that contain 
no extractable text.
'''

from pathlib import Path 
from langchain_community.document_loaders import ( PyPDFLoader ) 

# ======================================== 
# SPECIFY PDF FILE 
# ======================================== 

pdf_path = ( 
Path(__file__).resolve().parent / "library_notice_three_pages.pdf" ) 

# ======================================== 
# CREATE PAGE-WISE PDF LOADER 
# ======================================== 

loader = PyPDFLoader( file_path=str(pdf_path), mode="page" ) 

# ======================================== 
# PROCESS PDF PAGES LAZILY 
# ======================================== 

processed_pages = 0 

for document in loader.lazy_load(): 
    processed_pages += 1 
    page_number = ( document.metadata["page"] + 1 ) 
    text = " ".join( document.page_content.split() ) 
    print( "\nPAGE", page_number ) 
    print( "---------------------" ) 
    if text: 
        print( "STATUS: Text extracted" ) 
        print( "CONTENT:", text ) 
    else: 
        print( "STATUS: No extractable text" ) 
    print( 
    "Check whether the page is blank," 
    " scanned, or requires a different" 
    " extraction approach." ) 
    
    # ======================================== 
    # DISPLAY TOTAL 
    # ======================================== 
    print( "\nTOTAL PAGES PROCESSED" ) 
    print( "---------------------" ) 
    print( processed_pages ) 