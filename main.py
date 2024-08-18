# main.py

from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
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

    # Manually format the prompt with the template
    country = "France"
    prompt = prompt_template.format(country=country)

    # Get response from the OpenAI model using the invoke method
    try:
        response = openai_model.invoke(prompt)
        print(f"Response from OpenAI model: {response}")
    except Exception as e:
        print(f"Error running the model: {e}")

if __name__ == "__main__":
    explore_langchain()
