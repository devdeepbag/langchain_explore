# main.py

from langchain_openai import OpenAI
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

    # Example: Using OpenAI model
    print("\nExploring OpenAI model...")
    try:
        openai_model = OpenAI(api_key=openai_api_key)
    except Exception as e:
        print(f"Error initializing OpenAI model: {e}")
        return

    # Define a prompt template
    prompt_template = PromptTemplate(template="What is the capital of {country}?")

    # Create an LLM chain with OpenAI model and prompt template
    try:
        llm_chain = LLMChain(
            llm=openai_model,
            prompt=prompt_template  # Update to `prompt` if `prompt_template` is deprecated
        )
    except Exception as e:
        print(f"Error creating LLMChain: {e}")
        return

    # Run the chain
    country = "France"
    try:
        response = llm_chain.run(country=country)
        print(f"Response from OpenAI model: {response}")
    except Exception as e:
        print(f"Error running the chain: {e}")

if __name__ == "__main__":
    explore_langchain()
