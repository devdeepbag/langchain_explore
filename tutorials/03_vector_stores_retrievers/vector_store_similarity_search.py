from main import *


# Similarity search with score
print(vectorstore.similarity_search_with_score("salmon"))

# Embedded query

embedding = OpenAIEmbeddings().embed_query("cat")

print(vectorstore.similarity_search_by_vector(embedding))