from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic'],
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text'],
)


model = AzureChatOpenAI(
    api_key=os.getenv("AZURE_API_KEY"),
    model='gpt-4o-mini',
    azure_endpoint=os.getenv("AZURE_ENDPOINT"),
    openai_api_version="2024-08-01-preview",
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser
result = chain.invoke({'topic':'cricket'})
print(result)