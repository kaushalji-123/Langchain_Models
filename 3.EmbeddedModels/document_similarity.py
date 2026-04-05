from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=300)

document = ["The capital of India is New Delhi.",
           "Lucknow is the capital of Uttar Pradesh",
            "Mumbai is the capital of Maharashtra"]
query = "What is the capital of Mumbai?"

document_embeddings = embeddings.embed_documents(document)
query_embedding = embeddings.embed_query(query)
similarity_scores = cosine_similarity([query_embedding], document_embeddings)[0]

result = sorted(list(enumerate(similarity_scores)),key=lambda x:x[1])[-1]

index, score = result  
print(query)
print (document[index])
print("Similarity Scores:", similarity_scores)
 
