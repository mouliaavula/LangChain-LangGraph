import os
from  langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

llm = ChatOpenAI(model='gpt-4o-mini',api_key=os.getenv("OPENAI_API_KEY"))
prompt_template = PromptTemplate.from_template("Explain {topic} in simple english")
topic = input("Enter topic: ")
prompt = prompt_template.invoke(
    {
        #"topic":topic
        #"subject":topic
        #if input variable did not match
        #KeyError: "Input to PromptTemplate is missing variables {'topic'}.  Expected: ['topic'] Received: ['subject']
        
        #if no input variable 
        # KeyError: "Input to PromptTemplate is missing variables {'topic'}.  Expected: ['topic'] Received: []
    }
)

response = llm.invoke(prompt)
print(response.content)
