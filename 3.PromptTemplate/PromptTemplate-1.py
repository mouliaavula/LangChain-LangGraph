import os
from langchain_core.prompts import PromptTemplate

'''
PromptTemplate is a LangChain class used to create reusable prompts with variables 
that can be filled with different values at runtime.

PromptTemplate is a LangChain class used to create reusable text based dynamic prompts.
'''

prompt_template = PromptTemplate.from_template("Explain {topic} in simple english")

#print(type(prompt_template))
# o/p: <class 'langchain_core.prompts.prompt.PromptTemplate'>
#print(prompt_template)
# o/p: input_variables=['topic'] input_types={} partial_variables={} template='Explain {topic} in simple english'
#print(prompt_template.input_variables)
# o/p: ['topic']
'''
prompt_template.invoke() is used to take values for input variables in a prompt template 
and  generate formatted final prompt that can be passed to the LLM

input type of prompt_template.invoke() is dict
'''
result = prompt_template.invoke(
    {
        "topic":"Python" #the value is hardcoded
    }
)
print(type(result))
# o/p:<class 'langchain_core.prompt_values.StringPromptValue'>
print(result)
# o/p:text='Explain Python in simple english'
print(result.text)
#o/p:Explain Python in simple english
print(result.to_string())
# o/p:Explain Python in simple english
#================================================================================================
'''
str() is a built-in Python function used to convert an object into a string.
str(object)
    ↓
calls object's __str__() method

__str__() is a special method that you can define inside your class, to decide how an object should be represented as a string, on call print(object)

if we do not define , it inherits Object class __str__ method as Object class is parent for all user defined classes

to_string() is not a standard Python built-in function.
It is usually a method provided by a particular library/class.
print(result.to_string())--->provided by langchain

here result is of type <class 'langchain_core.prompt_values.StringPromptValue'> so to_string() is StringPromptValue method


str() is the function you normally call. 

__str__() is the special method Python uses to decide how an object should be represented as a string. 

to_string() is library/class-specific and is not a general Python equivalent of str().
'''

#======================================================================================================
'''
Very important: prompt_template.invoke() vs llm.invoke()
prompt_template.invoke()--->It fills the template.
llm.invoke()--->It sends the final prompt to the LLM.
'''
#=====================================================================================================

'''
prompt_template = PromptTemplate(
    template="Explain {topic} in simple English.",
    input_variables=["topic"]
)
is same as below 
prompt_template = PromptTemplate.from_template(
    "Explain {topic} in simple English."
)

'''





