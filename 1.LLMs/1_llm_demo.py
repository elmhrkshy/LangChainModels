from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

llm = OpenAI(model='gpt-3.5-turbo-instruct')

llm_response = llm.invoke("What is the capital of India?")

print(llm_response)
