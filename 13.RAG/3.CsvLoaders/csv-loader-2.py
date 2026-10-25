'''
Objective: Read an actual CSV file and observe how its data rows become LangChain Document objects.
'''
from pathlib import Path
from langchain_community.document_loaders import CSVLoader
#=============================================================================================
# Create Sample CSV file
#=============================================================================================
file_path = Path(__file__).resolve().parent/'students_2.csv'

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
csv_loader = CSVLoader(file_path=file_path,encoding='utf-8')

#=============================================================================================
# Load CSV documents
#=============================================================================================
documents = csv_loader.load()

#=============================================================================================
# Display document count
#=============================================================================================

print("\n =======================================================================")
print("\n Total documents:", len(documents))

#=============================================================================================
# Display each document
#=============================================================================================

for number, document in enumerate(documents,start=1):
    print("\nDocument Number")
    print("------------------------------------------------------------------")
    print("Page Content:")
    print(document.page_content)
    print("\n Source:")
    print(Path(document.metadata['source']).name)
    print("Row Index:",document.metadata['row'])
    




