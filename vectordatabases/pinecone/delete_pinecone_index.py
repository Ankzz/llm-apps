import os

from pinecone import Pinecone

pc = Pinecone(os.environ.get("PINECONE_API_KEY"))
pc.delete_index("my-index")
