import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import (SystemMessage, HumanMessage)

llm  = ChatOpenAI(model='gpt-4o-mini',api_key=os.getenv('OPENAI_API_KEY'))

# Keep system message separately
system_message = SystemMessage(
    content="""
    You are a helpful AI assistant. Answer in simple english
    """
    )

# Complete conversation history
history = []
MAX_MESSAGES = 6

while True:
    user_input = input("\n You:")
    if user_input.lower() == "exit":
        print("Chat Ended")
        break
    # Add user message to history
    history.append(HumanMessage(content=user_input))
    
    # Select recent history
    recent_history = history[-MAX_MESSAGES:]
    
    # Add system message always
    input_messages = [
        system_message,
        *recent_history
    ]
    #Send selected history to model
    response = llm.invoke(input_messages)
    
    print("\n AI response:",response.content)
    
    # Add AI response to history
    history.append(response)
    print("\n Total stored messages: ",len(history))
    print("\n Recent conversation messages: ",len(recent_history))
    print("\n Total messages sent to model: ",len(input_messages))