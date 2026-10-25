import json
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    message_to_dict,
    messages_from_dict
)

#1 Create Langchain messages
messages = [
    HumanMessage(content="My name is Mouli."),
    AIMessage(content="Nice to meet you, Mouli")
]

print("===========Original messages========")
for message in messages:
    print(type(message).__name__,":",message.content)
    
#2 Messages to Python Dictionaries

serialized = [message_to_dict(message) for message in messages]   
print("====Python Dictionaries========") 
print(serialized)

#3 Python dictionaries to Json string 

json_string = json.dumps(serialized,indent=2)

print("============Json String=====================")
print(json_string)

#4 json string to python dictionaries

python_data = json.loads(json_string)

print("=========Back to python dictionaries=======")
print(python_data)

#5 Python dictionaries to langchain messages
restored_messages = messages_from_dict(python_data)

print("====Restored messages=============")
for message in restored_messages:
    print(type(message).__name__,":",message.content)