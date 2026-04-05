from langchain_huggingface import ChatHuggingFace , HuggingFacePipeline

import os
os.environ['HF_HOME'] = 'D:/huggingFace_cache'  # Set the Hugging Face cache director

llm = huggingface_pipeline = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task='text-generation',
    pipeline_kwargs=dict(max_new_tokens= 1000, temperature= 0.7)
)
model = ChatHuggingFace(llm=llm)
result = model.invoke("im runnig late for work, can you write a message to my boss to inform him about this?")
print(result.content)
