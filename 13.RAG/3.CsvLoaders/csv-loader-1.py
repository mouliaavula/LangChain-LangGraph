from langchain_community.document_loaders import CSVLoader

#============================================================================
# Create csv loader
#============================================================================
# csv_loader = CSVLoader(file_path='students.csv') should work but seeing some special character in Student_ID
csv_loader = CSVLoader(file_path='students.csv',encoding='utf-8')

#============================================================================
# Load CSv documents
#============================================================================
documents = csv_loader.load()

#============================================================================
# Display document count
#============================================================================

print("\n Total Documents: ",len(documents))

#============================================================================
# Display each  document
#============================================================================

for document in documents:
    print("\n============================================================")
    print("\nPage Content")
    print(document.page_content)
    print("page content type")
    print(type(document.page_content))
    print("\n Metadata")
    print(document.metadata)
    