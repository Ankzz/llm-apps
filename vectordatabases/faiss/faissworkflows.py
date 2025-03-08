from langgraph.graph import StateGraph
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_openai import OpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.retrievers import BM25Retriever
from langchain.schema import Document

import os

# Set api-key
self_api_key = os.getenv("OPENAI_API_KEY")
if self_api_key is None or self_api_key == "":
     self_api_key = os.environ.get("OPENAI_API_KEY")

# Step 1: Load Data & Initialize Components
docs = ["Artificial Intelligence is transforming the world.",
        "Faiss is a powerful library for fast similarity search.",
        "BM25 is a strong keyword-based retrieval technique.",
        "Hybrid search combines vector search and lexical search."]

# Convert text to LangChain Document objects
documents = [Document(page_content=text) for text in docs]

# Initialize OpenAI embeddings
embeddings = OpenAIEmbeddings(api_key=self_api_key)

# Create FAISS index
vector_store = FAISS.from_documents(documents, embeddings)

# Initialize BM25 keyword retriever
bm25_retriever = BM25Retriever.from_documents(documents)

# Initialize LLM
llm = OpenAI(api_key= self_api_key, model="gpt-3.5-turbo-instruct")

# Initialize Langchain with the Gemini API key
# google_llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Define StateGraph Workflow
class RAGState:
    query: str
    faiss_results: list
    bm25_results: list
    reranked_results: list
    final_answer: str

    def __init__(self, query:str=None, faiss_results:list =None,
                 bm25_results:list =None, reranked_results:list=None, final_answer:str=None):
        self.query = query
        self.faiss_results = faiss_results
        self.bm25_results = bm25_results
        self.reranked_results = reranked_results
        self.final_answer = final_answer
        pass

workflow = StateGraph(RAGState)


# Step 2: Vector Search Node (FAISS)
def vector_search(state):
    query = state.query
    retriever = vector_store.as_retriever(search_k=3)
    faiss_results = retriever.invoke(query)
    return {"faiss_results": faiss_results}


workflow.add_node("vector_search", vector_search)


# Step 3: BM25 Keyword Search Node
def keyword_search(state):
    query = state.query
    bm25_results = bm25_retriever.invoke(query)
    return {"bm25_results": bm25_results}


workflow.add_node("keyword_search", keyword_search)


# Step 4: Merge & Re-rank Results Node
def rerank_results(state):
    combined_results = state.faiss_results + state.bm25_results
    unique_results = {doc.page_content: doc for doc in combined_results}.values()

    # Use LLM to re-rank documents
    prompt_template = """Given the query: {query}, rank the following documents in order of relevance:

    {documents}

    Return the top-ranked document."""

    prompt = PromptTemplate.from_template(prompt_template)
    formatted_prompt = prompt.format(query=state.query,
                                     documents="\n".join([doc.page_content for doc in unique_results]))

    best_doc = llm.invoke(formatted_prompt)
    return {"reranked_results": [best_doc]}


workflow.add_node("rerank_results", rerank_results)


# Step 5: Generate Final Answer
def generate_answer(state):
    context = state.reranked_results[0] if state.reranked_results else "No relevant information found."
    prompt = f"Based on the following document:\n\n{context}\n\nAnswer the user's query: {state.query}"
    final_answer = llm.invoke(prompt)
    return {"final_answer": final_answer}


workflow.add_node("generate_answer", generate_answer)

# Define Execution Edges (Flow of the Workflow)
workflow.add_edge("vector_search", "rerank_results")
workflow.add_edge("keyword_search", "rerank_results")
workflow.add_edge("rerank_results", "generate_answer")

# Define Input & Output
workflow.set_entry_point("vector_search")
workflow.set_entry_point("keyword_search")
workflow.set_finish_point("generate_answer")

# Compile & Run
app = workflow.compile()
input_query = "How does hybrid search work?"
result = app.invoke({"query": input_query})
print("\n🔹 Final Answer:", result["final_answer"])
