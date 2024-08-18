"""
serve.py

This script sets up a FastAPI server to deploy the LangChain application as a REST API using LangServe. 
The application translates text from English to a specified language. The server allows the LangChain chain to be accessed via HTTP requests, 
making it available as a simple chatbot interface.

Key Components:
- FastAPI: Hosts the API server.
- ChatPromptTemplate: Formats the input prompt.
- OpenAI: Generates the translation using the OpenAI API.
- StrOutputParser: Extracts the string response from the model's output.
- LangServe: Integrates the chain into the FastAPI app and serves it at /chain.

Run the server and access the chatbot at http://localhost:8000/chain/playground/.
"""

#!/usr/bin/env python
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import OpenAI
from langserve import add_routes
import os
from dotenv import load_dotenv

# Load environment variables from a .env file to securely manage API keys and other settings
load_dotenv()

# 1. Create prompt template
# Define a system message template for instructing the model on the task
system_template = "Translate the following into {language}:"
# Combine the system message with user input using ChatPromptTemplate
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

# 2. Create model
# Initialize the OpenAI model with the API key loaded from the environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')
model = OpenAI(api_key=openai_api_key)

# 3. Create parser
# Initialize an output parser to extract the string from the model's response
parser = StrOutputParser()

# 4. Create chain
# Chain together the prompt template, model, and output parser to form the application logic
chain = prompt_template | model | parser

# 5. App definition
# Create a FastAPI instance to serve the application as an API
app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple API server using LangChain's Runnable interfaces",
)

# 6. Adding chain route
# Use LangServe to add the chain to the FastAPI app, making it accessible via the /chain endpoint
add_routes(
    app,
    chain,
    path="/chain",
)

# Run the FastAPI server using Uvicorn when the script is executed directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
