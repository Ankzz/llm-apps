"""
@author: Ankit .<ankzzdev@gmail.com>

Pinecone is a vector database that’s optimized for similarity search, often used in applications like semantic search,
recommendation systems, and machine learning. Pinecone efficiently handles high-dimensional vector embeddings and
performs fast, scalable similarity searches.

Key Features of Pinecone
    Fast and scalable vector search.
    Managed infrastructure with automatic scaling.
    Easy-to-integrate APIs.
    Supports large-scale data with low latency.
    Key Parameters to Tune in Pinecone
    When setting up and optimizing your Pinecone index, you can fine-tune various parameters to improve performance and accuracy.

Index Creation Parameters
These parameters are specified when creating an index:

Parameter	Description	                                                                                Recommended Values
metric	    Distance metric for similarity search. Options: cosine, euclidean, or dotproduct.	        Choose based on your data type and model output.
pod_type	Defines the hardware type (e.g., p1, s1). Higher types improve speed and capacity.	        p1.x1, p1.x2, s1.x1, etc.
dimension	Number of dimensions in your vectors. This must match the output size of your embedding model.	Depends on your embedding model (e.g., OpenAI = 1536).
pods	    Number of pods in your index for scaling. More pods increase capacity and throughput.	    Start small, scale as needed.
replicas	Number of replicas for redundancy and higher availability.	                                For production, consider at least 2.
metadata_config	Enables filtering on custom metadata.	                                                JSON structure defining searchable metadata fields.

Query Parameters
When querying the Pinecone index, these parameters improve search results:

Parameter	        Description	                                                        Recommended Usage
top_k	            Number of top-ranked results to return. Higher values may reduce performance.	10–100 for balanced performance.
include_metadata	Returns associated metadata with results. Useful for enriching results.	Use True when metadata is relevant.
include_values	    Returns the original vector values.	Avoid unless you need raw vectors.
filter	            Filters search results based on metadata conditions.	Use when metadata conditions are required.
Metadata Filtering
    Pinecone’s metadata filtering allows you to narrow down results using conditions like:

    Equality: { "category": "electronics" }
    Range: { "price": { "$gt": 100 } }
    Logical Operators: { "$and": [ { "price": { "$lt": 500 } }, { "brand": "Sony" } ] }

Best Practices for Tuning
✅ Select the right metric:
cosine → Best for text embeddings.
dotproduct → Great for normalized vectors.
euclidean → Useful for geometric data.
✅ Optimize top_k: Avoid unnecessarily high values — 20-50 often balances accuracy and performance.
✅ Manage pods and replicas: Scale pods for higher throughput; replicas improve fault tolerance.
✅ Leverage filter conditions: Use metadata filtering to reduce search space and improve query speed.
✅ Batch Inserts: For bulk data uploads, batch data to reduce API calls and improve speed.

"""

import os

from pinecone import Pinecone
from pinecone import ServerlessSpec

pc = Pinecone(os.environ.get("PINECONE_API_KEY"))

# Embed data
data = [
    {"id": "vec1", "text": "Apple is a popular fruit known for its sweetness and crisp texture."},
    {"id": "vec2", "text": "The tech company Apple is known for its innovative products like the iPhone."},
    {"id": "vec3", "text": "Many people enjoy eating apples as a healthy snack."},
    {"id": "vec4", "text": "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."},
    {"id": "vec5", "text": "An apple a day keeps the doctor away, as the saying goes."},
]

embeddings = pc.inference.embed(
    model="llama-text-embed-v2",
    inputs=[d['text'] for d in data],
    parameters={
        "input_type": "passage"
    }
)

vectors = []
for d, e in zip(data, embeddings):
    vectors.append({
        "id": d['id'],
        "values": e['values'],
        "metadata": {'text': d['text']}
    })

pc. create_index(
 name='my-index', dimension=1024, metric='cosine',
    spec=ServerlessSpec(cloud='aws', region='us-east-1'))

print(pc.describe_index('my-index'))

index = pc.Index(name='my-index',
                                host=pc.describe_index('my-index').host)

index.upsert(
    vectors=vectors,
    namespace="ns1"
)

# pc.delete_index('my-index')