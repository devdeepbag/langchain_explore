import os

from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve the API key from the .env file and set it as an environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please ensure the .env file contains the OPENAI_API_KEY.")

os.environ["OPENAI_API_KEY"] = api_key

from langchain_core.documents import Document
from langchain_community.document_loaders import DirectoryLoader, TextLoader


# Same documents
documents = [
    Document(
        page_content="Dogs are great companions, known for their loyalty and friendliness.",
        metadata={"source": "mammal-pets-doc"},
    ),
    Document(
        page_content="Cats are independent pets that often enjoy their own space.",
        metadata={"source": "mammal-pets-doc"},
    ),
    Document(
        page_content="Siamese cats are a striking and elegant breed known for their sleek, slender bodies, almond-shaped blue eyes, and short, glossy coats. Their distinctive color points—ears, face, paws, and tail—are typically darker than the rest of their cream or white bodies, creating a unique contrast that sets them apart from other breeds. Siamese cats are not just known for their beauty but also for their highly social and affectionate nature. They are often described as vocal and playful, with a strong tendency to form close bonds with their human companions. Intelligent and curious, Siamese cats thrive on interaction and are often seen as one of the more \"talkative\" breeds, engaging in conversation-like meows with their owners.",
        metadata={"source": "mammal-pets-doc"},
    ),
    Document(
        page_content="Goldfish are popular pets for beginners, requiring relatively simple care.",
        metadata={"source": "fish-pets-doc"},
    ),
    Document(
        page_content="Parrots are intelligent birds capable of mimicking human speech.",
        metadata={"source": "bird-pets-doc"},
    ),
    Document(
        page_content="Rabbits are social animals that need plenty of space to hop around.",
        metadata={"source": "mammal-pets-doc"},
    ),
]


# Instantiate a vector store
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.runnables import RunnableLambda

vectorstore = Chroma.from_documents(
    documents,
    embedding=OpenAIEmbeddings(),
)


