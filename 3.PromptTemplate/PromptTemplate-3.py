import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
llm = ChatOpenAI(model='gpt-4o-mini',api_key = os.getenv("OPENAI_API_KEY"))
prompt_template = PromptTemplate.from_template("Explain {topic} in simple english")
topic = input("Enter Topic:")
result = prompt_template.invoke(
    {
        "topic":topic
    }
)
ai_ms = llm.invoke(result)
print(ai_ms.content)
# User ---> PromptTemplate --->Final Prompt -->LLM --->AIMessage -->Response