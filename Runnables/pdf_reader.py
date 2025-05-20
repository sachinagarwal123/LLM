from langchain.embeddings import AzureOpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import openai
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

loader = TextLoader("/Users/sachinagarwal/Desktop/langchain_learning/LLM/bb.txt")
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

embedding = AzureOpenAIEmbeddings(model="text-embedding-ada-002",api_key=os.getenv("AZURE_API_KEY"),azure_endpoint=os.getenv("AZURE_ENDPOINT"))
vectorstore = FAISS.from_documents(docs, embedding)
retriever = vectorstore.as_retriever()
query = "What is the main topic of the document?"
retriever_docs =  retriever.get_relevant_documents(query)

retrieved_text = "\n".join([doc.page_content for doc in retriever_docs])

llm = openai(
    api_key=os.getenv("AZURE_API_KEY"),
    model='gpt-4o-mini',
    azure_endpoint=os.getenv("AZURE_ENDPOINT"),
    openai_api_version="2024-08-01-preview",
)

prompt = f"Based on the following text, answer the question: {query}\n\n{retrieved_text}"
answer = llm.predict(prompt)
print(answer)
print("Answer:", answer)
print("Retrieved Text:", retrieved_text)
print("Retrieved Documents:", retriever_docs)
print("Retrieved Documents Content:", [doc.page_content for doc in retriever_docs])
print("Retrieved Documents Metadata:", [doc.metadata for doc in retriever_docs])
print("Retrieved Documents IDs:", [doc.id for doc in retriever_docs])