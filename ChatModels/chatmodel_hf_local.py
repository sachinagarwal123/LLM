from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="meta-llama/Llama-2-7b-chat-hf",
    task="text-generation",
    pipeline_kwargs=dict(temperature=0.7,
    max_new_tokens=256
    )
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("What is the capital of India?")
print(result.content)