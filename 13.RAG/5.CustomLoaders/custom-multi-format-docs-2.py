'''
 Handling Zero-Based Page and Row Metadata
'''
from importlib import metadata
from xml.dom.minidom import ElementInfo

from langchain_core.documents import Document

#==========================================================================
#Create sample documents
#==========================================================================
documents = [
    Document(
        page_content='Employee Leave policy.',
        metadata={
            'source':'policy.pdf',
            'page':0
        }
    ),
    
    Document(
            page_content='name:ravi',
            metadata={
                'source':'students.csv',
                'row':0
            }
        ),
    Document(
                page_content='Library opens at 8 am.',
                metadata={
                    'source':'library.txt'
                }
            )
]


#==========================================================================
#Inspect source meta data
#==========================================================================

for document in documents:
    metadata = document.metadata
    print("\nSource:",metadata['source'])
    page_index = metadata.get('page')
    row_index = metadata.get('row')
    
    if page_index is not None:
        print("\nDisplay Page:", page_index+1)
    elif row_index is not None:
        print("\nDisplay row:", row_index+1)
    else:
        print("\nPage/Row is not applicable")



'''
Program Explanation
-------------------
Friends, observe the first Document.
Its page index is zero.

But our application correctly displays:
Page 1

The second Document has row index zero.
We display:
Row 1
The third Document has neither page nor row metadata.
Therefore, we display:
Not applicable

Main Conclusion:
---------------
Correct metadata handling preserves zero-based indexes while presenting user-friendly page and row numbers.
'''



'''
Note:
The Python zip() function pairs up corresponding elements from two or more iterables (like lists, tuples, etc.) and returns an iterator of tuples.

eg:
names = ["Ravi", "Priya", "Rahul"]
marks = [90, 85, 95]

result = zip(names, marks) #Returns a zip object

print(type(result)) #zip object
print(result)
print(list(result))

<class 'zip'>
<zip object at 0x000002A9E3D4B440>
[('Ravi', 90), ('Priya', 85), ('Rahul', 95)]
'''
