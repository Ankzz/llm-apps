from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.docstore.document import Document
from langgraph.graph import StateGraph, END

embedding_model = HuggingFaceEmbeddings(
    model_name = "all-MiniLM-L6-v2")

# Sample documents
docs = [
    Document(page_content="Artificial Intelligence is transforming industries."),
    Document(page_content="Machine Learning is a subset of AI focused on learning patterns."),
    Document(page_content="Natural Language Processing enables AI to understand human language."),
    Document(page_content="Ankit is a good boy!"),
]

# Convert documents to FAISS index
faiss_index = FAISS.from_documents(docs, embedding_model)

# --- Step 2: Define LangGraph Workflow ---
class RAGState:
    query: str
    result: str

    def __init__(self, query=None, result=None):
        self.query = query
        self.result = result

graph = StateGraph(RAGState)

# Node: Embedding Search
def retrieve(state):
    query_embedding = embedding_model.embed_query(state.query)
    retrieved_docs = faiss_index.similarity_search_by_vector(query_embedding, k=3)
    return RAGState(query=state.query, result="\n".join([doc.page_content for doc in retrieved_docs]))

graph.add_node("retriever", retrieve)
graph.set_entry_point("retriever")
graph.add_edge("retriever", END)

# --- Step 3: Run the Graph ---
app = graph.compile()

query_input = RAGState("Tell me about AI.")
output = app.invoke(query_input)

print(f"\n🔹 Retrieved Documents:\n{output['result']}")
