"""
@author: Ankit .<ankzzdev@gmail.com>

ChromaDB is an open-source vector database designed specifically for storing and querying
high-dimensional embeddings, commonly used in machine learning, AI applications, and search
systems. It excels in efficiently handling unstructured data such as text, images, audio,
and video by leveraging vector similarity search.

Common Use Cases
✅ Retrieval-Augmented Generation (RAG): Enhances LLMs by retrieving relevant context from a vector database.
✅ Semantic Search: Enables intelligent search over unstructured data like documents, images, and videos.
✅ Recommendation Systems: Efficiently suggests products, content, or media based on vector similarity.
✅ Anomaly Detection: Identifies unusual patterns or outliers by comparing vectors.

Why Use ChromaDB?
✅ Easy-to-use API with minimal learning curve.
✅ High-performance search across large-scale data.
✅ Flexible enough for both on-device and cloud deployment.
✅ Suitable for modern AI pipelines requiring fast and accurate retrieval.

"""
import chromadb

# Initialize ChromaDB client
client = chromadb.Client()

# Create a collection
collection = client.create_collection(name="my_collection")

# Add some data (with embeddings)
collection.add(
    embeddings=[[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]],
    documents=["Document 1", "Document 2"],
    metadatas=[{"source": "source1"}, {"source": "source2"}],
    ids=["id1", "id2"]
)

# Query the collection
results = collection.query(
    query_embeddings=[[0.1, 0.2, 0.7]],
    n_results=1
)

print("Query Results:", results)