import os
from dotenv import load_dotenv
from langchain_openai import OpenAI


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = OpenAI(model="omni-moderation-latest",temperature=0.6, api_key=OPENAI_API_KEY) # 0-> not creative 1-> very creative(might give wrong information)

name = llm("I want to open a restaurant, suggest a fancy name.")

print(name)