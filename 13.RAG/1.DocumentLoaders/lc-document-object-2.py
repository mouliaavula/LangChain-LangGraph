'''
Objective: Maintain actual text with source, department and year information.
'''

from langchain_core.documents import Document

#=======================================================================================
# Create Document with Meta data
#=======================================================================================

document = Document(
    page_content='The office opens at 9 AM.',
    metadata = {
        "source":"office_rules.txt",
        "department":"Administration",
        "year":2026
    }
)

#=======================================================================================
# Access Page content
#=======================================================================================

print("Page Content")
print("=============================================================================")
print(document.page_content)



#=======================================================================================
# Access Complete metadata
#=======================================================================================

print("Meta data")
print("=============================================================================")
print(document.metadata)



#=======================================================================================
# Access individual metadata fields
#=======================================================================================

print("\n Source")
print("=============================================================================")
print(document.metadata['source'])


print("\n department")
print("=============================================================================")
print(document.metadata['department'])


print("\n year")
print("=============================================================================")
print(document.metadata['year'])