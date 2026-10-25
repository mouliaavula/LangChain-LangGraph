'''
Objective: Create several Documents, maintain them in one list 
and display their information. 
'''

from langchain_core.documents import Document

#========================================================================================
# Create First Document
#========================================================================================

document1 = Document(
    page_content='The library opens at 8 AM.',
    metadata={
        "source":"library_rules.txt"
    }
)



#========================================================================================
# Create Second Document
#========================================================================================

document2 = Document(
    page_content='Student must wear their ID card.',
    metadata={
        "source":"student_rules.txt"
    }
)


#========================================================================================
# Create Third Document
#========================================================================================

document3 = Document(
    page_content='Fee must be paid before deadline.',
    metadata={
        "source":"fee_rules.txt"
    }
)

#========================================================================================
# Store documents in list
#========================================================================================

documents = [
    document1,
    document2,
    document3
]

print("\n Total documents:",len(documents))


#========================================================================================
# Display Document Information
#========================================================================================

# if we do not provide start =1 , it will take default from 0
for number, document in enumerate(documents,start=1):
    print("\n Document:",number)
    print("Content:",document.page_content)
    print("Source:",document.metadata['source'])