'''
Objective: Create multiple student information documents and 
display their content and metadata. 
'''

from langchain_core.documents import Document

#=====================================================================================
# Create Student information documents
#=====================================================================================
documents = [
    Document(
        page_content='Admissions start 1 November 2026',
        metadata = {
            'source':"admission_notice.txt",
            'department':"Admissions"
        }
    ),
    
    Document(
        page_content='The library open from 8 am to 6 pm',
        metadata={
            'source':'library_notice.txt',
            'department':'Library'
        }
    )
]

#=====================================================================================
# Display total documents
#=====================================================================================

print("'\n Student Information packet")
print("===================================================================================")
print("Total documents:",len(documents))


#=====================================================================================
# Display every document
#=====================================================================================

for number , document in enumerate(documents, start=1):
    print("\n Document:",number)
    print("Content:",document.page_content)
    print("Source:",document.metadata.get('source','Unknown'))
    print("Department:",document.metadata.get('department','Not Specified'))
