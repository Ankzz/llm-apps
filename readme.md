# 🚀LLM Art Corner

![alt text](LLMArtCorner.png "LLM Art Corner")

### This repository serves as a sandbox for experimenting with various Large Language Models (LLMs) and related technologies, such as vector databases, while remaining open to broader innovations.

#### While we focus on all aspects of AI based application development - currently our efforts is towards Vectordatabases.

### FAISS 

#### Faiss is a popular vectordatabase with a wide-spread implementation.
#### From Faiss perspective covered items are:
> L2Flat Indexing

> IVF Indexing

> HNSW Indexing

> Performance comparison of all listed methods

> Workflow - achieved using Langchain and Faiss


> ### Note:
> All these tests and development has been conducted over:
>> 2 Core (4 Core with Hyper-threading)
> 
>> 16 GB RAM
> 
>> Windows 11


### To build or test all the implementations provided. 
1. Please go to vectordatases/ folder
2. Either execute locally or over a platform any of the vector databases

## Following are the list of Databases being evaluated.
| **Database**      |
|-------------------|
| **Pinecone**      | 
| **FAISS**         |
| **Milvus**        |
| **Weaviate**      |
| **ChromaDB**      |
| **Qdrant**        |
| **Annoy**         |
| **Redis**         |
| **Elasticsearch** |
| **ScaNN**         |
| **MongoDB Atlas** |


### Parameters against which these databases are being evaluated.
| **Parameters**               |
|------------------------------|
| **Managed Service**          |
| **Indexing support**         |
| **Workload supportaibality** |
| **Serach results**           |

---
### Each folder has its own readme file detailing out advantages and scenarios best suited for the application of that database
---

# Vectordatabases

---
Apart from **FAISS** and **Pinecone**, there are several other powerful vector databases designed for fast and scalable similarity search. Each offers unique strengths in terms of performance, scalability, and deployment flexibility.

---

## 🔎 **Top Vector Databases for Similarity Search**

### **1. Milvus**
✅ **Open-source** and scalable vector database.  
✅ Designed for handling large-scale datasets with billions of vectors.  
✅ Provides features like **sharding**, **replication**, and **dynamic schema**.  
✅ Supports integrations with PyTorch, TensorFlow, and Hugging Face.

**Use Case:** Ideal for large-scale recommendation systems and AI-driven search.  

---

### **2. Weaviate**
✅ An open-source, **schema-free** vector search engine.  
✅ Supports hybrid search (vector + keyword search).  
✅ Offers **real-time updates** and a **GraphQL API** for queries.  
✅ Supports **vectorizers** like OpenAI, Cohere, and Hugging Face directly.  

**Use Case:** Great for combining text, image, and structured data in search.  

---

### **3. ChromaDB**
✅ Open-source and built specifically for **AI-native applications**.  
✅ Simple Python API for fast integration.  
✅ Supports **metadata filtering** and **embeddings storage**.  
✅ Commonly used with **LLM apps** like RAG (Retrieval-Augmented Generation).  

**Use Case:** Best for AI chatbots, LLM-powered search, and dynamic content retrieval.  

---

### **4. Qdrant**
✅ Open-source vector search engine with **high performance**.  
✅ Features include **payload filtering**, **distributed deployment**, and **scalability**.  
✅ Written in Rust for optimal performance.  

**Use Case:** Suitable for real-time applications like fraud detection or recommendation engines.  

---

### **5. Annoy (Approximate Nearest Neighbors Oh Yeah)**
✅ Developed by Spotify, designed for **fast, read-only** search.  
✅ Lightweight, efficient, and ideal for **low-memory environments**.  
✅ Best suited for in-memory indexing of vectors.  

**Use Case:** Best for fast, static data lookups with low-latency requirements.  

---

### **6. Redis (with Vector Search Module)**
✅ Redis offers a **Search & Query** module (e.g., `RediSearch`).  
✅ Enables fast similarity search directly inside Redis.  
✅ Suitable for apps that need fast indexing alongside real-time data.  

**Use Case:** Great for combining vector search with structured data queries.  

---

### **7. Elasticsearch (with Dense Vector Fields)**
✅ Elasticsearch offers a **k-NN search** feature.  
✅ Effective for combining vector search with text-based search.  
✅ Best suited for integrating **semantic search** with traditional keyword search.  

**Use Case:** Ideal for hybrid search use cases in enterprise applications.  

---

### **8. Vespa**
✅ Open-source engine optimized for **large-scale machine learning inference**.  
✅ Supports **vector search**, **tensor search**, and **complex data structures**.  
✅ Offers high performance for large-scale recommendation systems.  

**Use Case:** Best for e-commerce, content recommendation, and personalized search.  

---

### **9. ScaNN (Scalable Nearest Neighbors)**
✅ Developed by Google, optimized for **high-speed** and **low-latency** search.  
✅ Provides efficient ANN search with **quantization** for memory efficiency.  
✅ Designed for **in-memory** search on large datasets.  

**Use Case:** Best for applications requiring ultra-fast query responses.  

---

### **10. ElasticSearch k-NN (Dense Vector Search)**
✅ Popular for combining **vector search** with traditional search capabilities.  
✅ Provides flexible filtering, ranking, and sorting mechanisms.  

**Use Case:** Ideal for applications that combine semantic and keyword search.  

---

## ⚙️ **Choosing the Right Vector Database**
| **Database**   | **Best For**                 | **Key Strength** |
|----------------|------------------------------|-------------------|
| **Pinecone**      | Cloud-based apps, SaaS tools | Fully managed with minimal setup |
| **FAISS**          | On-premise, academic use     | Fast, memory-efficient, open-source |
| **Milvus**         | Large-scale enterprise data  | Highly scalable with distributed support |
| **Weaviate**       | Hybrid search + metadata     | Native NLP integration |
| **ChromaDB**       | AI-native applications       | Simple Python API for RAG |
| **Qdrant**         | Real-time, high-traffic data | Fast Rust-based performance |
| **Annoy**           | Lightweight static data      | Low memory footprint |
| **Redis**           | Real-time structured data    | Combines caching + vector search |
| **Elasticsearch**   | Semantic + text search       | Robust query capabilities |
| **ScaNN**           | High-speed in-memory search  | Lightning-fast performance |

---

## 🚀 Utilize this info as per your need