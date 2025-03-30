import time

import faiss

documents = [
    "Artificial Intelligence is transforming the world.",
    "Machine learning is a subset of AI.",
    "Deep learning models require large amounts of data.",
    "Faiss is an efficient similarity search library.",
    "Natural Language Processing enables machines to understand human language."
]

from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
documents_vectors = (
    model.encode(documents, convert_to_numpy=True).astype('float32'))

# Define vector dimension
d = documents_vectors.shape[1]

# Set Raw Faiss with L2 Indexing
index = faiss.IndexFlatL2(d)
index.add(documents_vectors)

# Set the IVF Indexing
quantizer = faiss.IndexFlatL2(d)

# Set the number of clusters expected
nlist = 3
index_ivf = faiss.IndexIVFFlat(quantizer, d, nlist)

index_ivf.train(documents_vectors)
index_ivf.add(documents_vectors)

# Set the HNSW Indexing
M = 16
index_hnsw = faiss.IndexHNSWFlat(d, M)
index_hnsw.add(documents_vectors)

#----------------------------------------------------------------------@
query_text = "AI is transforming industries."
query_vector = model.encode([query_text], convert_to_numpy=True).astype('float32')

k = 3  # Number of results to fetch

# Brute Force Search
start = time.time()
dist_flat, idx_flat = index.search(query_vector, k)
end = time.time()
print(f"\nFlat Search Time: {end - start:.5f} sec")

# IVF Search
start = time.time()
index_ivf.nprobe = 5  # Number of clusters to search in IVF
dist, idx_ivf = index_ivf.search(query_vector, k)
end = time.time()
print(f"IVF Search Time: {end - start:.5f} sec")

# HNSW Search
start = time.time()
dist_hnsw, idx_hnsw = index_hnsw.search(query_vector, k)
end = time.time()
print(f"HNSW Search Time: {end - start:.5f} sec")

# Print Results
print("\nResults:")
print("Flat:", [documents[i] for i in idx_flat[0]])
print("IVF:", [documents[i] for i in idx_ivf[0]])
print("HNSW:", [documents[i] for i in idx_hnsw[0]])