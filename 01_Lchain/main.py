from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate


llm = OllamaLLM(model="llama3.2")

prompt_template_name = PromptTemplate(
    input_variables=["cuisine"],
    template = "I want to open a cafe for {cuisine} foods/snacks, suggest only one fancy name for this. please give only one name."
)

name_chain = prompt_template_name | llm

prompt_template_item = PromptTemplate(
    input_variables=["restaurant_name"],
    template = "Suggest some menu items for the {restaurant_name}. Return it as comma seperated items."
)
item_chain = prompt_template_item | llm
# result = chain.invoke({"cuisine": "Indian"})

# Step 4: Compose the full pipeline manually
restaurant_name = name_chain.invoke({"cuisine": "Mexican"}).strip()
print(f"Suggested name: {restaurant_name}")
    
# Second step: get menu items based on the name
menu_items = item_chain.invoke({"restaurant_name": restaurant_name}).strip()
print(f"Menu items: {menu_items}")
