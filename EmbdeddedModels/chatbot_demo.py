from langchain_openai import AzureOpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os

load_dotenv()

embedding = AzureOpenAIEmbeddings(model="text-embedding-ada-002",api_key=os.getenv("AZURE_API_KEY"),azure_endpoint=os.getenv("AZURE_ENDPOINT"))
documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]
query = 'rohit'

doc_embeddings = embedding.embed_documents(documents)
query_embedding =  embedding.embed_query(query)

scores = cosine_similarity([query_embedding],doc_embeddings)[0]
index,score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]
print(query)
print(documents[index])
print("similarity score is",score)


