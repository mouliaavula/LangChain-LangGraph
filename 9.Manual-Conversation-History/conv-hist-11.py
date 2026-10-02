import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import (
    SystemMessage, HumanMessage
)

llm = ChatOpenAI(model='gpt-4o-mini',api_key=os.getenv('OPENAI_API_KEY'))

# System message, keep separately
system_message = SystemMessage(
    content="""
    You are a helpful AI Assistant. Answer in simple English
    """)
# Complete chat conversation history
history = []
MAX_MESSAGE = 6

while True:
    user_input = input("\nYou:")
    if user_input.lower() == "exit":
        print("Chat Ended")
        break
    # Add user message to history
    history.append(HumanMessage(content=user_input))
    # select recent conversation
    recent_history = history[-MAX_MESSAGE:]
    # Always include system message
    # * is unboxing i.e all messages are extracted and added to new input_messages list
    input_messages = [
        system_message,
        *recent_history
    ]
    # Send selected context to model
    response = llm.invoke(input_messages)
    print("\n AI response is :",response.content)
    
    # Add AI response to complete history
    history.append(response)