'''
Objective: Separate selected CSV fields into page_content and metadata.
'''
from pathlib import Path
from langchain_community.document_loaders import CSVLoader
#=============================================================================================
# Create Sample CSV file
#=============================================================================================
file_path = Path(__file__).resolve().parent/'students_3.csv'

file_path.write_text(
    "Student_ID,Name,Course,Fee\n"
    "S101,Mouli,Python,10000\n"
    "S102,Manish,GenAI,15000\n"
    "S103,Neethu,ML,20000\n"
    "S104, Sravan,FSDS,30000\n",
    encoding='utf-8'
)

#=============================================================================================
# Create  CSV loader
#=============================================================================================

csv_loader = CSVLoader(file_path=str(file_path),
                       encoding='utf-8',
                       metadata_columns=['Student_ID','Course'],
                       content_columns=['Name','Fee'])

#=============================================================================================
# Load documents
#=============================================================================================
documents = csv_loader.load()

#=============================================================================================
# Display Results
#=============================================================================================

print("\n Total Documents:",len(documents))

for number, document in enumerate(documents,start=1):
    print("\nDocument Number:", number)
    print("===================================================================")
    print("Page content")
    print(document.page_content)
    print("\nMetadata")
    print("Student ID:",document.metadata['Student_ID'])
    print("Course:",document.metadata['Course'])
    print("Source:", document.metadata['source'])
    print("Row Index:", document.metadata['row'])
    
# Note: CSVLoader still provides source and row information    
    
    

