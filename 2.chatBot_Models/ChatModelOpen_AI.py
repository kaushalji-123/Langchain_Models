from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4", temperature=1.6, max_completion_tokens=100)
result = llm.invoke("write me 5 line of song any the mmake me happy?")
print(result.content)   