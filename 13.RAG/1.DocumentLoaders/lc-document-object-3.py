'''
Objective: Safely access metadata fields that may not exist.
'''

from langchain_core.documents import Document

document = Document(
    page_content='Students must carry their ID card.',
    metadata={
        "source":"college_notice.txt",
        "department":"Student Services"
    }
)

#===============================================================================
# Access existing metadata
#===============================================================================

print("\n Source")
print("=========================================================================")
print(document.metadata['source'])


print("\n Department")
print("=========================================================================")
print(document.metadata['department'])

#===============================================================================
# Access missing  metadata safely
#===============================================================================

# Author does not exists in document so if we access like document.metadata['author']
# we get key error to avoid that  use below and it is safest way always instead document.metadata['source']

print("\n Author")
print("=========================================================================")
print(document.metadata.get('author',"Not available"))

# with get method if meta data does not exists then we can provide our custom default value like "Not Available"
