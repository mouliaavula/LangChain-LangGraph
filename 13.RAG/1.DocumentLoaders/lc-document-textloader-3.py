from pathlib import Path
from langchain_community.document_loaders import TextLoader

#==============================================================================================
# Create demo folder with name : day2_notices
#==============================================================================================

base_dir = Path(__name__).resolve().parent/'day2_notices'

base_dir.mkdir(exist_ok=True)

#==============================================================================================
# Create 3 text files
#==============================================================================================

file_data = {
        'student_rules.txt':'Students must cary their ID cards.',
        'library_notice.txt':'The Library closes at 8 pm.',
        'fee_notice.txt':'Course fee dead line is 15th November 2026'
}

for file_name, content in file_data.items():
    file_path = base_dir/file_name
    file_path.write_text(content,encoding='utf-8')

all_documents = []

for file_name in file_data:
    file_path = base_dir/file_name
    loader = TextLoader(file_path=str(file_path),encoding='utf-8')
    
    documents = loader.load()
    all_documents.extend(documents)

#==============================================================================================
# Display total documents
#==============================================================================================

print("\n Total documents:",len(all_documents))

#==============================================================================================
# Display each document
#==============================================================================================


for number, document in enumerate(all_documents,start=1):
    print("Source:",Path(document.metadata['source']).name)
    print("Content:",document.page_content)
    
    # We can use TextLoader repeatedly to convert information from multiple text files 
    # into a collection of LangChain Document objects.
    
    