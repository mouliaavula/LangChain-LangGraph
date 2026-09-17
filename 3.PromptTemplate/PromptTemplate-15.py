import os 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

"""
# This is langchain concept to pass default values by using partial variables

template = PromptTemplate.from_template("Explain {topic} at {level} level",
                                        partial_variables={
                                            "topic":"Python",
                                            "level": "Beginner"
                                        })

# Here we are passing one input variable topic so other input variable level is taken from partial variables
prompt = template.invoke({
    "topic":"java"
})

print(prompt.to_string())
# o/p: Explain java at Beginner level
"""
#==============================================================================================================
"""
# In partial variables it is not compulsory to define default values for all input variables

template = PromptTemplate.from_template("Explain {topic} at {level} level",
                                        partial_variables={
                                            "topic":"Python"
                                        })
prompt = template.invoke({
    "level":"Beginner" # this is needed bec we do not define default value for level
})

print(prompt.to_string())

"""
#=============================================================================================================
"""
template = PromptTemplate.from_template("Explain {topic} at {level} level",
                                        partial_variables={
                                            "topic":"Python"
                                        })
#topic = input("Enter topic: ")
prompt = template.invoke({
    #"topic":topic,
    "level":"Beginner" # this is needed bec we do not define default value for level
})

print(prompt.to_string())

"""
# ==============================================================================================================

template = PromptTemplate.from_template("Explain {topic} at {level} level",
                                        partial_variables={
                                            "topic":"Python"
                                        })
topic = input("Enter topic: ")
prompt = template.invoke({
    "topic":topic,
    "level":"Beginner" # this is needed bec we do not define default value for level
})

print(prompt.to_string())
