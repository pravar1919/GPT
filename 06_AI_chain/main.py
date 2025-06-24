from langchain.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv
from langchain_community.llms import HuggingFaceHub
from langchain_huggingface import HuggingFaceEndpoint
load_dotenv()

import os
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGING_FACE_API_KEY")

import langchain
langchain.debug = True

llm = llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    task="text-generation",
    temperature=0.5, 
    max_new_tokens=512
)

# Define LLM
# llm = OllamaLLM(model="llama3.2")

# Doctor Agent
doctor_prompt = PromptTemplate(
    input_variables=["patient_info"],
    template="""
    You are a medical doctor. The patient condition is: {patient_info}.
    Provide diagnosis, medication advice, and precautions.
    """
)
doctor_chain = doctor_prompt | llm

# Dietician Agent
dietician_prompt = PromptTemplate(
    input_variables=["doctor_advice"],
    template="""
    Based on this medical advice: {doctor_advice}.
    Provide a suitable meal plan considering common dietary restrictions.
    """
)
dietician_chain = dietician_prompt | llm

# Fitness Trainer Agent
trainer_prompt = PromptTemplate(
    input_variables=["dietician_advice"],
    template="""
    Based on this meal plan and medical advice: {dietician_advice}.
    Suggest suitable exercises and physical precautions.
    """
)
trainer_chain = trainer_prompt | llm

# Example Input
input_text = "A 60-year-old male undergoing radiotherapy for prostate cancer."

# Run Chains Sequentially and Collect Responses
# Step 1: Doctor
doctor_response = doctor_chain.invoke({"patient_info": input_text})

# Step 2: Dietician
dietician_response = dietician_chain.invoke({"doctor_advice": doctor_response})

# Step 3: Fitness Trainer
trainer_response = trainer_chain.invoke({"dietician_advice": dietician_response})

# Final Combined Output
final_result = {
    "Doctor's Advice": doctor_response,
    "Dietician's Meal Plan": dietician_response,
    "Fitness Trainer's Suggestions": trainer_response
}

# Print Outputs
for section, response in final_result.items():
    print(f"\n===== {section} =====\n")
    print(response)
