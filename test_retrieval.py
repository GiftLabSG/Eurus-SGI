from helper_functions.retriever import get_retriever
from langchain_openai import ChatOpenAI

# Define your test query
test_query = "How to apply for the Career Conversion Programme for Security Officers"

# Load retriever filtered by CCP for Security Officers
retriever = get_retriever(grant_filter="Career Conversion Programme for Security Officers")

# Fetch top documents
docs = retriever.get_relevant_documents(test_query)

# Display results
print("\n📄 Retrieved Documents:\n")
for i, doc in enumerate(docs, 1):
    print(f"--- Document {i} ---")
    print(doc.page_content[:1000])  # Print only first 1000 characters for readability
    print("\nMetadata:", doc.metadata)
    print("\n")
