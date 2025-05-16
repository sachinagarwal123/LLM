from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()
model = ChatAnthropic(model="claude-3.5-sonnet-20241022",temperature=1,max_completion_tokens=1)
result = model.invoke("what is the capital of india?")
print(result)
print(result.content)
