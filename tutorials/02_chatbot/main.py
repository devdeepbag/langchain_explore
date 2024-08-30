import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.chat_history import (
    BaseChatMessageHistory,
    InMemoryChatMessageHistory,
)
from langchain_core.runnables.history import RunnableWithMessageHistory


# Load environment variables from the .env file
load_dotenv()

# Retrieve the API key from the .env file and set it as an environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please ensure the .env file contains the OPENAI_API_KEY.")

os.environ["OPENAI_API_KEY"] = api_key

# Initialize the ChatOpenAI model
model = ChatOpenAI(model="gpt-3.5-turbo")

# Define a session history store and a function to retrieve session history
store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    """
    Retrieve or create a new chat history for a given session ID.
    
    Args:
        session_id (str): The session identifier.
    
    Returns:
        BaseChatMessageHistory: The chat message history for the session.
    """
    if session_id not in store:
        print(f"Creating new chat history for session: {session_id}")
        store[session_id] = InMemoryChatMessageHistory()
    else:
        print(f"Retrieving existing chat history for session: {session_id}")
    return store[session_id]


#########
# Starting chat1 - simple Q&A with memory
#########

# Define the configuration to be passed into the RunnableWithMessageHistory
config = {"configurable": {"session_id": "chat1"}}

# Create a RunnableWithMessageHistory instance to handle chat sessions
with_message_history = RunnableWithMessageHistory(model, get_session_history)

# Store a message in the first session
response = with_message_history.invoke(
    [HumanMessage(content="Hi! I'm Bob")],
    config=config,
)

# Verify that the initial message is stored in the first session
# print("Session abc1 history:", store["abc1"].messages)

# Now, send another message to check it remembers you
response = with_message_history.invoke(
    [HumanMessage(content="What's my name?")],
    config=config,
)

# Verify chat history
print("Session chat1 history:", store["chat1"].messages)

