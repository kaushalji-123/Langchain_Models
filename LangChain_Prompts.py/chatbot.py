from langchain_openai import ChatOpenAI   
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model="gpt-4")

Chat_history = [
    SystemMessage(content="You are a helpful assistant that provides concise and accurate responses to user queries.")
]

while True:
    user_input = input("User: ")
    Chat_history.append(HumanMessage(content=user_input))
         
    if user_input == "exit":
        print("Exiting the chatbot. Goodbye!")
        break
    response = model.invoke(Chat_history)
    Chat_history.append(AIMessage(content=response.content))
    print("Chatbot:", response.content)
print("Chat history:", Chat_history)

