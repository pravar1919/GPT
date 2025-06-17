For this I am using llama3.2 model.
This model is running locally on my machine.
using `ollama run llama3.2`

Next I have used `langchain-ollama` library to setup the initial code.
1. Initializing the Ollama class
2. Setup the prompt template ( this is like fstring ).
    - here I am asking for the restaurant name
3. Sequential chain
    - It is like to generate menu for the same restaurant.