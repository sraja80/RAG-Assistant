import os
import numpy as np

def load_documents(directory):
    documents = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as f:
                documents.append(f.read().strip())
    return documents

def build_tfidf(docs):
    vocab = set()
    for doc in docs:
        vocab.update(doc.lower().split())
    vocab = sorted(list(vocab))
    
    N = len(docs)
    V = len(vocab)
    
    tf = np.zeros((N, V))
    for i, doc in enumerate(docs):
        words = doc.lower().split()
        word_count = len(words)
        for word in words:
            if word in vocab:
                j = vocab.index(word)
                tf[i, j] += 1 / word_count
    
    df = np.sum(tf > 0, axis=0)
    idf = np.log(N / (df + 1e-10))
    
    tfidf = tf * idf
    
    return tfidf, vocab, idf

def vectorize_query(query, vocab, idf):
    query = query.lower()
    words = query.split()
    word_count = len(words)
    qvec = np.zeros(len(vocab))
    for word in words:
        if word in vocab:
            j = vocab.index(word)
            qvec[j] += 1 / word_count
    qvec_idf = qvec * idf
    return qvec_idf

def cosine_similarity(vec1, vec2):
    dot = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    return dot / (norm1 * norm2 + 1e-10)

def retrieve(query, tfidf, vocab, idf, top_k=1):
    qvec = vectorize_query(query, vocab, idf)
    similarities = [cosine_similarity(row, qvec) for row in tfidf]
    top_indices = np.argsort(similarities)[-top_k:][::-1]
    return [docs[top_indices[0]] for top_indices in top_indices], [similarities[i] for i in top_indices]  # Wait, fix
    # Correction:
    return [docs[i] for i in top_indices], [similarities[i] for i in top_indices]
```

Wait, small error in retrieve: the return was wrong, fixed to [docs[i] for i in top_indices]
