import sys
import numpy as np
from utils import build_tfidf, vectorize_query, cosine_similarity, retrieve, load_documents

def generate_response(query, retrieved_docs):
    context = "\n\n".join(retrieved_docs)
    # Mock generation: In a real system, use an LLM API here
    return f"Query: {query}\n\nRetrieved Context:\n{context}\n\nGenerated Answer: Based on the retrieved information, the answer to '{query}' is summarized from the context above."

def main():
    # Load documents from knowledge_base directory
    documents = load_documents('knowledge_base')
    
    if not documents:
        print("No documents found in knowledge_base directory.")
        sys.exit(1)
    
    # Precompute TF-IDF
    tfidf_matrix, vocabulary, idf_vector = build_tfidf(documents)
    
    print("Retrieval-Augmented AI Assistant: Type your question (or 'quit' to exit)")
    while True:
        query = input("Enter your question: ").strip()
        if query.lower() == 'quit':
            break
        if not query:
            continue
        retrieved_docs, scores = retrieve(query, tfidf_matrix, vocabulary, idf_vector, top_k=3)
        response = generate_response(query, retrieved_docs)
        print(response)
        print("\n---\n")

if __name__ == "__main__":
    main()
```
