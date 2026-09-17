from langchain_core.messages import SystemMessage
from langchain_core.messages import HumanMessage
from langchain_core.messages import AIMessage

# content is positional parameter so we may use keyword name or may not
system_message = SystemMessage(content="You are experienced python teacher")
print(system_message)
print(system_message.content)
print("\n\n")
human_message = HumanMessage("What is python")
ai_message = AIMessage("Python is a programming language")
print("\n\n")
print(human_message)
print(human_message.content)
print("\n\n")
print(ai_message)
print(ai_message.content)

