from langchain_openai import AzureChatOpenAI
import streamlit as st
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate,load_prompt
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
load_dotenv()

model = AzureChatOpenAI(
    api_key=os.getenv("AZURE_API_KEY"),
    model='gpt-4o-mini',
    azure_endpoint=os.getenv("AZURE_ENDPOINT"),
    openai_api_version="2024-08-01-preview",

)

chat_history = [
    SystemMessage(content="You are a helpful AI assistant."),
]


while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("Assistant:", result.content)

print("Chat history:",chat_history)
