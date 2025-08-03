from helper_functions.retriever import get_retriever

def test_retriever():
    question = "Tell me about the ctc grant"
    grant_filter = "Company Training Committee Grant"

    retriever = get_retriever(grant_filter=grant_filter)
    docs = retriever.invoke(question)  # ✅ Updated from get_relevant_documents()

    if not docs:
        print("⚠️ No documents found.")
    else:
        for i, doc in enumerate(docs, 1):
            print(f"\n📄 Document {i}")
            print(f"Source: {doc.metadata.get('source', 'Unknown')}")
            print(f"Grant Title: {doc.metadata.get('grant_title', 'Unknown')}")
            print(f"Content preview: {doc.page_content[:300]}...\n")

if __name__ == "__main__":
    test_retriever()