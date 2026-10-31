from importlib import metadata

from langchain_core.documents import Document

#======================================================================================
# Create Document
#======================================================================================

document = Document(
    page_content='Library closes at 6 PM.',
    metadata = {
        'source':'library_rules.txt'
    }
)

#======================================================================================
# Preserve Original metadata
#======================================================================================

original_metadata = document.metadata.copy()

#======================================================================================
# Add custom metadata
#======================================================================================

document.metadata.update({
    'source_type':'txt',
    'department':'Library',
    'category':'Notice'
})

#======================================================================================
# Display Results
#======================================================================================
meta_data = document.metadata
print('\nSource:',meta_data['source'])
print('\nSource type:',meta_data['source_type'])
print('\nDepartment:',meta_data['department'])
print('\nCategory:',meta_data['category'])
print('\nSource Preserved:',original_metadata['source']==meta_data['source'])

'''
Conclusion: We can enrich LangChain Document metadata while preserving source information.
'''






