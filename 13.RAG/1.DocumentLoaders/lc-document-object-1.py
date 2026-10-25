'''
Program 1 — Creating the First LangChain Document 
Objective: Create a Document object and access its content 
and metadata. 
'''

from langchain_core.documents import Document

# ============================================================================
# Create Document Object
#=============================================================================

document = Document(page_content="Python is a popular programming language")

# ============================================================================
# Access page content
#=============================================================================

print("\n Page Content")
print("========================================")
print(document.page_content)


# ============================================================================
# Access meta data
#=============================================================================

print("\n Meta data")
print("========================================")
print(document.metadata)

# ============================================================================
# Check object type
#=============================================================================

print("\n Object type")
print("========================================")
print(type(document).__name__)