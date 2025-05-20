from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = AzureChatOpenAI(
    api_key=os.getenv("AZURE_API_KEY"),
    model='gpt-4o-mini',
    azure_endpoint=os.getenv("AZURE_ENDPOINT"),
    openai_api_version="2024-08-01-preview",
)

prompt = PromptTemplate(
    input_variables=['topic'],
    template='Give 3 fact about {topic}',
)

topic = input("Enter a topic: ")
formatted_prompt = prompt.format(topic=topic)
print(formatted_prompt)
result = model.predict(formatted_prompt)
print(result)