'''
Objective: Load several files into one collection using a custom BaseLoader implementation.
'''

from importlib import metadata
from pathlib import Path
from langchain_core.document_loaders import BaseLoader
from langchain_core.documents import Document

#=====================================================================================================
# Custom Directory text loader
#=====================================================================================================
class FolderTextLoader(BaseLoader):
    def __init__(self,folder_path):
        self.folder_path = Path(folder_path)
    
    def lazy_load(self):
        for file_path in sorted(
            self.folder_path.glob('*.txt')
        ):
            content = file_path.read_text(encoding='utf-8')
            yield Document(page_content=content,
                           metadata={'source':str(file_path)})
            
#=====================================================================================================
# Prepare Sample files
#=====================================================================================================

folder =Path(__name__).resolve().parent/'sample_folder_files'
folder.mkdir(exist_ok=True)

files = {
    "admissions.txt": "Admissions start on Monday.",
    "library.txt": "Library opens at 8 AM.",
    "student_rules.txt": "Students must carry ID cards."
}

for filename, content in files.items():
    (folder/filename).write_text(content,encoding='utf-8')
    
#=====================================================================================================
# Load multiple text files
#=====================================================================================================    

loader = FolderTextLoader(folder_path=folder)
documents = loader.load()

#=====================================================================================================
# Display results
#=====================================================================================================

for number, document in enumerate(documents,start=1):
    print("\nDocument Number:",number)
    print("Source:", Path(document.metadata.get('source','Not available')))
    print("content: ",document.page_content)

