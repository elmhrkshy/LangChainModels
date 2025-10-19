from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

model = ChatOpenAI(model='gpt-4.1', temperature=1.5)

result = model.invoke("What is the capital of India?")

#print(result)
print(result.content)
