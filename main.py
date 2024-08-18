# main.py

from langchain import LangChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv

def explore_langchain():
    # Load environment variables from .env file
    load_dotenv()

    # Get API key from environment variables
    openai_api_key = os.getenv('OPENAI_API_KEY')
    if not openai_api_key:
        raise ValueError("API key for OpenAI is not set in the environment variables")

    # Initialize LangChain
    print("Initializing LangChain...")
    lc = LangChain()

    # Example: Using OpenAI model
    print("\nExploring OpenAI model...")
    openai_model = OpenAI(api_key=openai_api_key)

    # Define a prompt template
    prompt_template = PromptTemplate(template="What is the capital of {country}?")

    # Create an LLM chain with OpenAI model and prompt template
    llm_chain = LLMChain(llm=openai_model, prompt_template=prompt_template)

    # Run the chain
    country = "France"
    response = llm_chain.run(country=country)
    print(f"Response from OpenAI model: {response}")

    # Example: Demonstrating a different module or feature of LangChain
    # (Add more examples based on LangChain's features)

if __name__ == "__main__":
    explore_langchain()
