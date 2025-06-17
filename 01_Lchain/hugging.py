from langchain_community.llms import HuggingFaceHub
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["HUGGINGFACEHUB_API_TOKEN"] =  os.getenv("HUGGING_FACE")
# HUGGING_FACE = os.getenv("HUGGING_FACE")

llm = HuggingFaceHub(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    model_kwargs={"temperature": 0.7, "max_new_tokens": 256}
)

print(llm("Explain how a transformer works."))
