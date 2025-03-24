from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

# Initialize client
client = QdrantClient("localhost", port=6333)

# Create a collection
client.create_collection(
    collection_name="my_collection",
    vectors_config={"size": 3, "distance": "Cosine"}  # Vector size and similarity metric
)

# Insert sample data
client.upsert(
    collection_name="my_collection",
    points=[
        PointStruct(id=1, vector=[0.1, 0.2, 0.3], payload={"category": "A"}),
        PointStruct(id=2, vector=[0.4, 0.5, 0.6], payload={"category": "B"})
    ]
)

# Query for nearest neighbors
query_results = client.search(
    collection_name="my_collection",
    query_vector=[0.1, 0.2, 0.3],
    limit=2
)

print("Search Results:", query_results)
