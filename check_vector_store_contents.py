from langchain_chroma import Chroma
from helper_functions.vectorstore import embedding, persist_directory

# Load the vectorstore
db = Chroma(persist_directory=persist_directory, embedding_function=embedding)

# Access raw documents
collection = db.get()

# Show total count
print(f"\n✅ Total documents in vectorstore: {len(collection['documents'])}")

# Show some metadata
for i, meta in enumerate(collection["metadatas"]):
    print(f"\n📄 Document {i+1}")
    print(f"Grant Title   : {meta.get('grant_title', 'N/A')}")
    print(f"Source        : {meta.get('source', 'N/A')}")
    print(f"Preview       : {collection['documents'][i][:300]}...\n")

    if i >= 9:  # Only show first 10 docs
        break