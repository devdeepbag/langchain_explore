"""
main.py

This script demonstrates the use of LangChain to create a simple application that translates text from English to a specified language.
It uses a prompt template, an OpenAI model, and an output parser to format the input, generate a response, and extract the relevant output.
The result is displayed in the console.

For an interactive chatbot, see serve.py

Key Components:
- ChatPromptTemplate: Formats the input prompt.
- OpenAI: Generates the translation using the OpenAI API.
- StrOutputParser: Extracts the string response from the model's output.
"""

from langchain_openai import OpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up OpenAI API key
openai_api_key = os.getenv('OPENAI_API_KEY')

# Initialize OpenAI model
openai_model = OpenAI(api_key=openai_api_key)

# Define system message template and user message template
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_template),
    ("user", "{text}")
])

# Initialize output parser to extract the string response
parser = StrOutputParser()

# Combine the model with the prompt template and output parser
chain = prompt_template | openai_model | parser

# Example input
language = "French"
text = "What a wonderful world!"
result = chain.invoke({"language": language, "text": text})

print(f"Translated text: {result}")


