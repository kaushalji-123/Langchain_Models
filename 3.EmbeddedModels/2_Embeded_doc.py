from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32)

document = ["The capital of India is New Delhi.",
           " lucknnow is the capital  of Uttar Pradesh",
              "Mumbai is the capital of Maharashtra"]
result = embeddings.embed_documents(document)
print(str(result))

