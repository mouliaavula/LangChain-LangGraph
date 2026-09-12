import os
from langchain_core.prompts import PromptTemplate
prompt_template = PromptTemplate.from_template("Explain {topic} in simple english")

#print(type(prompt_template))
# o/p: <class 'langchain_core.prompts.prompt.PromptTemplate'>
#print(prompt_template)
# o/p: input_variables=['topic'] input_types={} partial_variables={} template='Explain {topic} in simple english'
#print(prompt_template.input_variables)
# o/p: ['topic']
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



