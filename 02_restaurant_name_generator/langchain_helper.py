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
    template = "Suggest some menu items for the {restaurant_name}. Return it as comma seperated items only, nothing else no suggestion or nothing."
)
item_chain = prompt_template_item | llm
# result = chain.invoke({"cuisine": "Indian"})


def generate_menu(cusine):
    restaurant_name = name_chain.invoke({"cuisine": cusine}).strip()
        
    menu_items = item_chain.invoke({"restaurant_name": restaurant_name}).strip()
    restaurant_name, menu_items = restaurant_name, menu_items
    return {
        "name": restaurant_name,
        "menu_items": menu_items
    }


if __name__ == '__main__':
    print(generate_menu("Indian"))