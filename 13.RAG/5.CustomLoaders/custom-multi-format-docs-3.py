'''
Objective: Add common metadata fields to Documents from different source types.
'''

from importlib import metadata
from pathlib import Path

from langchain_core.documents import Document

#===============================================================================================
#Sample document collection
#===============================================================================================

documents = [
    Document(
        page_content='Student must carry ID cards.',
        metadata={
            'source':'student_rules.txt'
        }
    ),
    
    Document(
            page_content='Employees Receives 12 casual leaves.',
            metadata={
                'source':'company_policy.pdf',
                'page':0
            }
        ),
    Document(
                page_content='name:mouli',
                metadata={
                    'source':'students.csv',
                    'row':0
                }
            )
    
]


# ========================================
# KNOWN APPLICATION INFORMATION
# ========================================


classifications = [
    ('txt','Administration'),
    ('pdf','HR'),
    ('csv','Admissions')
]

# ========================================
# STANDARDISE METADATA
# ========================================


for document, classification in zip(documents,classifications):
    source_type,department = classification
    document.metadata.update(
        {
            'source_type':source_type,
            'department':department,
            'document_name':Path(document.metadata['source']).name
        }
    )
    
    
# ========================================
# DISPLAY RESULTS
# ========================================
for document in documents:

    metadata = document.metadata

    print("\nNAME:", metadata["document_name"])

    print("TYPE:", metadata["source_type"])

    print("DEPARTMENT:", metadata["department"])

    print(
        "ORIGINAL SOURCE:",
        metadata["source"]
    )

'''
Note:
Metadata standardisation lets us give different Documents a consistent structure without losing their original source information.

'''
    
    