import os 
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

class ResumeInfo(BaseModel):
    name:str | None = Field(default=None, description='Candidate name if available')
    job_title:str | None = Field(default=None, description='Candidate job title if available')
    experience :str | None = Field(default=None, description='Candidate experience in years if available')
    skills:list[str] = Field(description='Skill set of candidate')
    email:str | None = Field(default=None, description='Candidate email if available')
    
llm = ChatOpenAI(model='gpt-5.6-luna',api_key=os.getenv("OPENAI_API_KEY"))

str_llm = llm.with_structured_output(ResumeInfo)
resume = input("Enter text:")

prompt = f"""
Extract information from the resume text.

Important:
- Use only information present in the text.
- Do not guess missing information.
- Return missing optional values as null.

Resume:
{resume}
"""

result = str_llm.invoke(prompt)

print("\nRESUME INFORMATION")
print("------------------")

print("Name       :", result.name)
print("Job Title  :", result.job_title)
print("Experience :", result.experience)
print("Skills     :", result.skills)
print("Email      :", result.email)
