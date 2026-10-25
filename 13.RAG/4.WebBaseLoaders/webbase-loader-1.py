from langchain_community.document_loaders import WebBaseLoader

url = "https://www.durgasoftonline.com/s/pages/new-batches/"

web_loader = WebBaseLoader(
    web_path=url
)

documents  = web_loader.load()

print("total documents: ",len(documents))
document  = documents[0]
print("\n Page content=========================================")
print(document.page_content)
print(document.metadata)
