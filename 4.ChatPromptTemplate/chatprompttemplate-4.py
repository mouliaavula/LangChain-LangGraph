import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate.from_messages(
    [
        ('system',
         """
         You are an expert {subject} teacher.
         Student level:{level},
         Language:{language}
         Your job is to teach concepts with easy examples
         """),
        ('human',
         """
         Teach me {topic}
         Requirements:
         1.Give simple definition
         2.Explain why it is required
         3.Give 5 important points
         4.Give 2 real life examples
         5.Mention common mistakes
         6.End with one line conclusion
         """),
    ]
)

subject = input("Enter Subject: ")
level = input("Enter level: ")
language = input("Enter language: ")
topic = input("Enter topic: ")

chat_prompt = chat_template.invoke({
    "subject":subject,
    "level":level,
    "language":language,
    "topic":topic
})

llm = ChatOpenAI(model='gpt-4.1-mini',api_key=os.getenv("OPENAI_API_KEY"))
response = llm.invoke(chat_prompt)
print(response.content)