"""
@author: Ankit .<ankzzdev@gmail.com>
@description:
This module presents an implementation of HNSW Flat Index

HNSW - Hierarchical Navigable Small World. HNSW is a graph based indexing method
used in Faiss.

### How HNSW Works
-------------------
HNSW builds a multi-layer graph where:
Each vector is connected to several nearest neighbors.
At higher layers, fewer connections exist, allowing fast global traversal.
At lower layers, more connections ensure fine-grained search.

When a query is made:
The algorithm starts at the highest layer and moves downward.
It progressively refines the search until it finds the closest neighbors in
the lowest layer.
The result is a fast, approximate search with high recall.

Key Parameters in HNSW
-------------------------
Parameter	    Description
--------------  ------------------------------------------------------
M	            Number of connections per node (higher = better recall,
                more memory usage).
efConstruction	Number of neighbors considered during index building
                (higher = better recall).
efSearch	    Number of neighbors considered during search
                (higher = more accurate, slower).

Advantages of HNSW
------------------
✅ Scalable – Handles millions of vectors efficiently.
✅ Fast Approximate Search – Much faster than brute-force methods like Flat L2.
✅ High Recall – Tunable parameters balance speed and accuracy.
✅ No Clustering Needed – Unlike IVF, HNSW doesn't require a pre-clustering step.

When to Use HNSW?
-----------------
✅ Large-scale similarity search where brute-force is too slow.
✅ Real-time applications needing fast query responses.
✅ High-dimensional data (e.g., embeddings, NLP, image search).

"""

import faiss

documents = [
    "Artificial Intelligence is transforming the world.",
    "Machine learning is a subset of AI.",
    "Deep learning models require large amounts of data.",
    "Faiss is an efficient similarity search library.",
    "Natural Language Processing enables machines to understand human language."
]

from sentence_transformers import SentenceTransformer
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

documents_vectors = model.encode(documents, convert_to_numpy=True).astype("float32")

d = documents_vectors.shape[1]

M = 16
index_hnsw = faiss.IndexHNSWFlat(d, M)
index_hnsw.add(documents_vectors)

print("HNSW index size:", index_hnsw.ntotal)

# Query a document
query_text = "AI is changing industries."
query_vector = model.encode([query_text], convert_to_numpy=True).astype('float32')

# Search for top 3 similar documents
k = 3
distances, indices = index_hnsw.search(query_vector, k)

# Display results
print("\nQuery:", query_text)
print("\nTop similar documents:")
for i, idx in enumerate(indices[0]):
    print(f"{i+1}. {documents[idx]} (Distance: {distances[0][i]:.4f})")
