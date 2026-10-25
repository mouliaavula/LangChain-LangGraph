import os

FOLDER_NAME = "chat_history_2"
os.makedirs(FOLDER_NAME,exist_ok=True)
print("Folder got created")

class Student:
    def get_name(self):
        return "Mouli"
    
s = Student()
print(s.get_name())    


class Student1:
    @property
    def get_name_one(self):
        return"Manu"
    
s1 = Student1()
print(s1.get_name_one)    


with open("file1.txt","w",encoding='utf-8') as file:
    file.write("Mouli learning langchain")
    
with open('file1.txt','r',encoding='utf-8') as f:
    data = f.read()
    print(data)    