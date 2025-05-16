from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

chat_template = ChatPromptTemplate.from_messages([
    ('system',"You are a helpful {domain} expert.")
    ('human',"Explain in simple terms what is{topic}"),
])

prompt = chat_template.invoke({'domain':'cricket','topic':'dusra'})
print(prompt)