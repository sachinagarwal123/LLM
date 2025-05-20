from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

prompt = PromptTemplate(
    template='Give 3 fact about {topic}',
    input_variables=['topic'],
)

model = AzureChatOpenAI(
    api_key=os.getenv("AZURE_API_KEY"),
    model='gpt-4o-mini',
    azure_endpoint=os.getenv("AZURE_ENDPOINT"),
    openai_api_version="2024-08-01-preview",
)

parser = StrOutputParser()

chain = prompt | model | parser
result = chain.invoke({'topic':'black hole'})
print(result)

chain.get_graph().print_ascii()