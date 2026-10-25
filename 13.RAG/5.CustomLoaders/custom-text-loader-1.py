'''
Objective: Create a reusable loader using the maintained BaseLoader interface.
'''
from importlib import metadata
from pathlib import Path
from langchain_core.document_loaders import BaseLoader
from langchain_core.documents import Document

#===================================================================================================
# Create Custom text Loader
#===================================================================================================

class SimpleTextLoader(BaseLoader):
    def __init__(self,file_path,encoding='utf-8'):
        self.file_path = Path(file_path)
        self.encoding = encoding
    
    
    
    def lazy_load(self):
        content = self.file_path.read_text(encoding=self.encoding)
        yield Document(page_content=content,metadata={'source':str(self.file_path)})


#===================================================================================================
# Create Sample file
#===================================================================================================

file_path = Path(__file__).resolve().parent/'library_rules.txt'
file_path.write_text(
    "Library opens at 8 AM.\n"
    "Library closes at 6 PM.\n",
    encoding="utf-8"
)

#===================================================================================================
# Use custom langchain loader
#===================================================================================================        

loader = SimpleTextLoader(file_path=file_path)

documents = loader.load()

#===================================================================================================
# Display Results
#===================================================================================================

print("\n return type: ",type(documents).__name__)
print("\nTotal documents: ", len(documents))
print("\nDocument type: ", type(documents[0]).__name__)
print("\nPage Content")
print(documents[0].page_content.strip())
print("\nSource: ",Path(documents[0].metadata['source']).name)

'''
Note:
1. We created SimpleTextLoader, our own implementation of LangChain's BaseLoader interface.
We implemented lazy_load().
We did not implement a separate load() method.
Why?
Because the maintained BaseLoader interface already provides it.

2. At the time of execution there is no deprecation warning.

Main Conclusion:
----------------
BaseLoader lets us build our own LangChain-compatible document loaders without depending on sunset community
integrations
'''
