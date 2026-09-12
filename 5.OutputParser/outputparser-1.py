
# Output processing : taking model output and converting or extracting it into required 
# form by our application

# output parser: it is a langchain component that processes model output and coverts it into a 
# useful form

# prompt-->chatmodel-->modeloutput-->outputparser-->useful output

# model understands the input and generates the output

# output parser receives model output --> process it --> returns required form



import os
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model='gpt-4.1-mini',api_key=os.getenv("OPENAI_API_KEY"))
response = llm.invoke("What is python ? Explain one sentence")
#print(type(response))
#print(response)
#print(response.content)
print("input tokens:",response.usage_metadata['input_tokens'])
print("output tokens:",response.usage_metadata['output_tokens'])
print("total tokens:",response.usage_metadata['total_tokens'])
print()
print()
print("Model provider:",response.response_metadata['model_provider'])
print("Model name:",response.response_metadata['model_name'])
