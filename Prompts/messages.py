from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()
model = AzureChatOpenAI(
    api_key=os.getenv("AZURE_API_KEY"),
    model='gpt-4o-mini',
    azure_endpoint=os.getenv("AZURE_ENDPOINT"),
    openai_api_version="2024-08-01-preview",

)

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What is the capital of India?"),
]

result = model.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)