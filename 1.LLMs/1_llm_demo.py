from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
# print(os.getenv("OPENAI_API_KEY"))
llm = ChatOpenAI(model="gpt-5.4-mini")
response = llm.invoke("give me the allu gobhi reciepie")
print(response.content)







