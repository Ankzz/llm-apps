"""
@author: Ankit .<ankzzdev@gmail.com>
@description:
This module presents an implementation for a Flat L2 Index FAISS

A Flat L2 Index in Faiss is a brute-force nearest neighbor search method that stores
all vectors explicitly and compares every query to all stored vectors using L2
(Euclidean) distance.

### Key Properties:
-------------------
Feature	                Description
----------------------  --------------------------------------------------
✅ Exact Search	        Finds the true nearest neighbors (not approximate).
✅ L2 Distance	        Uses Euclidean distance as a similarity metric.
✅ Brute Force	        Compares every query to all stored vectors.
✅ Memory Intensive	    Stores all vectors without compression.
✅ Slow for Large Data	Scales poorly as the number of vectors grows.

### When to Use Flat L2?
------------------------
✅ Best for small datasets where exact nearest neighbors are required.
✅ Baseline comparison for approximate methods.
❌ Not suitable for large-scale retrieval (millions of vectors) due to high computation costs.

"""

import faiss

documents = [
    "Artificial Intelligence is transforming the world.",
    "Machine learning is a subset of AI.",
    "Deep learning models require large amounts of data.",
    "Faiss is an efficient similarity search library.",
    "Natural Language Processing enables machines to understand human language."
]

# Store the actual doc for id to text reference
import pickle

doc_store = "faiss_storage/index_to_text.pkl"
try:
    with open(doc_store, "rb") as f:
        index_to_text = pickle.load(f)
except FileNotFoundError as e:
    index_to_text : list[str] = []
    pass

# Add to existing list of docs
[index_to_text.append(x) for x in documents]

# Create vectors
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
document_vectors = (
    model.encode(documents, convert_to_numpy=True).astype('float32'))

# Define vector dimension
d = document_vectors.shape[1]

# Create a Faiss index (L2 distance-based search)
import os
if os.path.exists("faiss_storage/faiss_index.bin"):
    index = faiss.read_index('faiss_storage/faiss_index.bin')
else:
    index = faiss.IndexFlatL2(d)

# Add document vectors to the index
index.add(document_vectors)
faiss.write_index(index, "faiss_storage/faiss_index.bin")

print(f"Total documents stored in index: {index.ntotal}")

# Query a document
query_text = "AI is changing industries."
query_vector = model.encode([query_text], convert_to_numpy=True).astype('float32')

# Search for top 3 similar documents
k = 3
distances, indices = index.search(query_vector, k)


with open(doc_store, 'wb') as fid:
    pickle.dump(index_to_text, fid)

# import pprint
# pprint.pprint(indices)
# pprint.pprint(index_to_text)

# Display results
print("\nQuery:", query_text)
print("\nTop similar documents:")
for i, idx in enumerate(indices[0]):
    print(f"{i+1}. {index_to_text[idx]} (Distance: {distances[0][i]:.4f})")
