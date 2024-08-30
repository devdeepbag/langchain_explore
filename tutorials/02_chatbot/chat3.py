from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.chat_history import (
    BaseChatMessageHistory,
    InMemoryChatMessageHistory,
)
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, trim_messages
from operator import itemgetter
from langchain_core.runnables import RunnablePassthrough

from tutorial_02_init import *


#########
# Starting chat3 - simple chat with prompt template with system prompt, parameters and memory
#########


config = {"configurable": {"session_id": "chat3"}}

trimmer = trim_messages(
    max_tokens=70,
    strategy="last",
    token_counter=model,
    include_system=True,
    allow_partial=False,
    start_on="human",
)

messages = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="hi! I'm bob"),
    AIMessage(content="hi!"),
    HumanMessage(content="I like vanilla ice cream"),
    AIMessage(content="nice"),
    HumanMessage(content="whats 2 + 2"),
    AIMessage(content="4"),
    HumanMessage(content="thanks"),
    AIMessage(content="no problem!"),
    HumanMessage(content="having fun?"),
    AIMessage(content="yes!"),
]

trimmer.invoke(messages)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Answer all questions to the best of your ability in {language}.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

chain = (
    RunnablePassthrough.assign(messages=itemgetter("messages") | trimmer)
    | prompt
    | model
)


with_message_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="messages",
)



## Checking if it remembers my name (it won't if max_tokens <70 in this example)
response = chain.invoke(
    {
        "messages": messages + [HumanMessage(content="what's my name?")],
        "language": "English",
    }
)
print(response.content)

## Checking if it remembers the following question
response = chain.invoke(
    {
        "messages": messages + [HumanMessage(content="what do you remember from our recent conversation?")],
        "language": "English",
    }
)
print(response.content)




# response = with_message_history.invoke(
#     {"messages": [HumanMessage(content="Hi! I'm Todd")], "language": "Middle English"},
#     config=config,
# )

# print(response.content)

# response = with_message_history.invoke(
#     {"messages": [HumanMessage(content="What's my name again?")], "language": "Middle English"},
#     config=config,
# )

# print(response.content)