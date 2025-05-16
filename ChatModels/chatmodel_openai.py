from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4",temperature=1.5,max_completion_tokens=2)
result = model.invoke("Write a poem about the sea.")
print(result)
print(result.content)