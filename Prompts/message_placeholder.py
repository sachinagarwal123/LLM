from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
#chat template 

chat_template = ChatPromptTemplate.from_messages([
    ('system',"You are a helpful customer support agent."),
    MessagesPlaceholder(variable_name="chat_history"),
    ('human',"{query}"),
    
])

#load chat history
chat_history = []
with open("chat_history.txt", "r") as file:
    chat_history.extend(file.readlines())

#create a prompt
prompt = chat_template.invoke({'chat_history': chat_history, 'query': "Where is my refund"})
print(prompt)