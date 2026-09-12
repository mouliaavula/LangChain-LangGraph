import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

template = PromptTemplate.from_template("Explain {topic} at {level} level")

# To pass default values
# Below is the python approach to pass default values

topic = input("Enter topic: ") or "Python"
level = input("Enter level: ") or "Beginner"

prompt = template.invoke({
    "topic":topic,
    "level":level
})

print(prompt.to_string())


#o/p: without any input both are taken as default
#Enter topic: 
#Enter level: 
#Explain Python at Beginner level

#o/p: with topic input and level are taken as default
#Enter topic: Java
#Enter level: 
#Explain Java at Beginner level

#o/p: with level input and topic are taken as default
#Enter topic: 
#Enter level: beginner
#Explain Python at beginner level