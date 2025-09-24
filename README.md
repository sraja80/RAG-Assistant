**README.md**
```markdown
# Retrieval-Augmented AI Assistant Project

This is a simple Python-based Retrieval-Augmented Generation (RAG) AI assistant. It uses TF-IDF for retrieval from a knowledge base of text documents and a mock generation step to produce responses.

## Setup Instructions

1. **Prerequisites**:
   - Python 3.6+
   - Install dependencies: `pip install -r requirements.txt`

2. **Knowledge Base**:
   - Place text files (.txt) in the `knowledge_base/` directory. Each file represents a document.

3. **Running the Assistant**:
   - Run `python main.py`
   - Enter questions; the system retrieves relevant documents and generates a response.
   - Type 'quit' to exit.

4. **Example Interaction**:
   ```
   Enter your question: What is the capital of France?
   Query: What is the capital of France?
   
   Retrieved Context:
   The capital of France is Paris. Paris is known for the Eiffel Tower and is a major cultural center in Europe.
   
   Generated Answer: Based on the retrieved information, the answer to 'What is the capital of France?' is summarized from the context above.
   ```

5. **Customization**:
   - Add more .txt files to `knowledge_base/` for expanded knowledge.
   - Adjust `top_k` in `retrieve` for more/less context.
   - Replace mock generation in `generate_response` with an LLM API (e.g., OpenAI) for better answers.
   - To support PDFs, install `pymupdf` and modify `load_documents` to extract text from PDFs.

## Notes
- Retrieval uses custom TF-IDF implementation with NumPy (no scikit-learn needed).
- For advanced retrieval, consider adding FAISS or embeddings (requires additional libs).
```
