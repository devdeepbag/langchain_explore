from langchain_core.messages import HumanMessage
from langchain_core.chat_history import (
    BaseChatMessageHistory,
    InMemoryChatMessageHistory,
)
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from tutorial_02_init import *

#########
# Starting chat2 - simple chat with prompt template with system prompt, parameters and memory
#########


config = {"configurable": {"session_id": "chat2"}}

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Answer all questions to the best of your ability in {language}.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

chain = prompt | model

with_message_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="messages",
)

response = with_message_history.invoke(
    {"messages": [HumanMessage(content="Hi! I'm Todd")], "language": "Middle English"},
    config=config,
)

print(response.content)

response = with_message_history.invoke(
    {"messages": [HumanMessage(content="What's my name again?")], "language": "Middle English"},
    config=config,
)

print(response.content)