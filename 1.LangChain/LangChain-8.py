import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o",api_key=OPENAI_API_KEY)
msgs = []
sys_msg = SystemMessage(content="You are a help assistant and answer in simple english and in concise way ")
msgs.append(sys_msg)

while True:
    question  = input("You: ")
    if question.lower() == 'exit':
        break
    msgs.append(HumanMessage(content=question))
    print('The Number of messages sending:', len(msgs))
    ai_msg = llm.invoke(msgs)
    msgs.append(ai_msg)
    print(ai_msg.content)
    
    # for new request/input/question , by passing previous all messages (system, human and ai messages) will make model 
    # to remember previous conversation history