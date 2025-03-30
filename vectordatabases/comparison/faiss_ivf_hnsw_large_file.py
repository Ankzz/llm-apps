import fitz
import pymupdf
from numpy import ndarray


def load_split(_pdf_path:str):
    """Loads a PDF and splits its content into lines."""
    doc:pymupdf.Document = fitz.open(_pdf_path)
    _lines = []
    print(f"Total Page Count in the doc: {doc.page_count}")
    _count = 0
    for page in doc:
        text = page.get_text("text")  # Extract text
        _lines.extend(text.split("."))  # Split into sentences
        _count +=1
        if _count==100:
            break
    return _lines

# Example usage
pdf_path = "2008_Book_TimeSeriesAnalysis.pdf"  # Replace with your actual file path
documents = load_split(pdf_path)

# Setup Faiss and store embeddings
#----------------------------------------------------------------------@
import faiss
import time

# Model for text embeddings
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Embedding creation
start = time.time()
documents_vectors:ndarray = model.encode(sentences=documents, batch_size= 50, convert_to_numpy=True).astype("float32")
end = time.time()
print(f"\nTotal Document Encoding Time: {end - start:.5f} sec")

# Store document shape
d = documents_vectors.shape[1]

start = time.time()
# Set the IVF Indexing
quantizer = faiss.IndexFlatL2(d)

# Set the number of clusters expected
nlist = 3
index_ivf = faiss.IndexIVFFlat(quantizer, d, nlist)

# IVF Index creation
index_ivf.train(documents_vectors)
index_ivf.add(documents_vectors)
end = time.time()
print(f"\nIVF_PQ Index creation Time: {end - start:.5f} sec")

# HNSW Index creation
M = 16
index_hnsw = faiss.IndexHNSWFlat(d, M)
start = time.time()
index_hnsw.add(documents_vectors)
end = time.time()
print(f"\nHNSW Index creation Time: {end - start:.5f} sec")
print("HNSW index size:", index_hnsw.ntotal)

#----------------------------------------------------------------------@
# Query a document
query_text = "Key points for Forecasting techniques."
query_vector = model.encode([query_text], convert_to_numpy=True).astype('float32')

# Search for top 3 similar documents
k = 3

# IVF_PQ Search
start = time.time()
index_ivf.nprobe = 5  # Number of clusters to search in IVF
dist, idx_ivf = index_ivf.search(query_vector, k)
end = time.time()
print(f"IVF Search Time: {end - start:.5f} sec")

# HNSW Search
start = time.time()
dist_hnsw, idx_hnsw = index_hnsw.search(query_vector, k)
end = time.time()
print(f"\nHNSW Search Time for {k} top records: {end - start:.5f} sec")

# Display results
print("\nQuery:", query_text)
print("\nTop similar documents:")
# for i, idx in enumerate(indices_hnsw[0]):
#     print(f"{i+1}. {documents[idx]} (Distance: {dist_hnsw[0][i]:.4f})")
# Print Results
print("\nResults:")
print("IVF:", [documents[i] for i in idx_ivf[0]])
print("HNSW:", [documents[i] for i in idx_hnsw[0]])
