from main import *

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo")

from langchain.chains import create_sql_query_chain

chain = create_sql_query_chain(llm, db)
response = chain.invoke({"question": "How many employees are there"})
print(response)

print('running one-off query...')
print('response:')
print(db.run(response))

print('\nquery prompt:\n')
chain.get_prompts()[0].pretty_print()

