from dotenv import load_dotenv
import os
import json
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()
key = os.getenv('GROQ_API_KEY')

llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    api_key=key,
    temperature=0.6)

def get_cuisine_and_items(user_cuisine): 
    prompt_name = PromptTemplate.from_template(
        """ 
        I want to open a restaurant for {cuisine} food. 
        Suggest a single fancy name for this, 
        with no explanation and no string quotes'
        """
    )

    prompt_menu = PromptTemplate.from_template(
        """ 
        Suggest some menu items for a restaurant called {restaurant_name}'. 
        Return it as a comma separated list. 
        It should always have between 5 and 8 items.
        I want the restaurant_name as one key value pair and the menu_items as the second.
        MUST BE IN JSON FORMAT
        NO PREAMBLE AND NO ```
        """
    )

    first_chain = prompt_name | llm
    second_chain = prompt_menu | llm
    response = second_chain.invoke(first_chain.invoke({'cuisine',user_cuisine})).content
    return json.loads(response)