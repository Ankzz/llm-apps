"""
@author: Ankit .<ankzzdev@gmail.com>

@description: This module demonstrates IVF Indexing under Faiss

IVF (Inverted File Indexing) is a clustering-based method in Faiss used for fast
approximate nearest neighbor (ANN) search. Instead of searching through all vectors,
it first narrows the search space by looking only in relevant clusters.

How IVF Indexing Works:
----------------------
K-Means Clustering:
The dataset is divided into K clusters using K-Means.
Each vector is assigned to the nearest cluster (centroid).

Efficient Search:
When a query is made, it is assigned to the nearest cluster(s).
The search is performed only within these clusters, reducing search complexity.

Faster Lookups:
Instead of brute-force searching all vectors (like Flat L2), IVF restricts the
search to a subset, making it significantly faster.

Key Parameters in IVF:
----------------------
Parameter	        Description
----------------    ---------------------
nc (num_clusters)	Number of clusters (higher = more precise, lower = faster).
nprobe	            Number of clusters searched at query time (higher = better recall, slower).
IndexIVFFlat	    Uses exact distances within each cluster (faster but large memory).
IndexIVFPQ	        Uses Product Quantization for memory-efficient search.

Advantages of IVF
✅ Fast Search – Searches in a subset of vectors rather than all.
✅ Memory Efficient – Especially when combined with PQ (Product Quantization).
✅ Scalable – Works well for millions of vectors.
✅ Flexible – Can be tuned with nprobe to balance speed vs. recall.

When to Use IVF?
Large-scale datasets where brute-force search is too slow.
Fast, approximate similarity search.
When you can afford slight accuracy trade-offs for better performance.

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

# Get the dimension of the vectors created
d = documents_vectors.shape[1]

quantizer = faiss.IndexFlatL2(d)

# Set the number of clusters expected
nlist = 3
index_ivf = faiss.IndexIVFFlat(quantizer, d, nlist)

index_ivf.train(documents_vectors)
index_ivf.add(documents_vectors)

faiss.write_index(index_ivf, "faiss_storage/faiss_ivf_index.bin")
print(f"Total documents stored in index: {index_ivf.ntotal}")

# Query a document
query_text = "AI is changing industries."
query_vector = model.encode([query_text], convert_to_numpy=True).astype('float32')

# Search for top 3 similar documents
k = 3
distances, indices = index_ivf.search(query_vector, k)

# with open(doc_store, 'wb') as fid:
#    pickle.dump(index_to_text, fid)

# import pprint
# pprint.pprint(indices)
# pprint.pprint(index_to_text)

# Display results
print("\nQuery:", query_text)
print("\nTop similar documents:")
for i, idx in enumerate(indices[0]):
    print(f"{i+1}. {documents[idx]} (Distance: {distances[0][i]:.4f})")
