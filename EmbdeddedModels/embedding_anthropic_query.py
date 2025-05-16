from langchain_anthropic import AnthropicEmbeddings
from dotenv import load_dotenv
load_dotenv()

embedding = AnthropicEmbeddings(model="claude-3.5", dimensions=32)
result = embedding.embed_query("Delhi is the capital of India")
print(result)
print(str(result))