from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()


llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
result = llm.invoke("write me 5 line of song any the mmake me happy")
print(result.content)
