import os
from langchain_huggingface import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGING_FACE_API_KEY")

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    task="text-generation",
    temperature=0.5, 
    max_new_tokens=512
)

prompt = PromptTemplate.from_template("Explain the benefits of exercise for {group}")
chain = prompt | llm

result = chain.invoke({"group": "heart patients"})
print(result)

