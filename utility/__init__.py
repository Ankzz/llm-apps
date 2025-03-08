import os.path

import faiss
from sentence_transformers import SentenceTransformer

class SelfFaiss(faiss):
    def __init__(self, persist=False, store_mappings=False, faiss_app:str=""):
        self.persist = persist
        self.store_mapping = store_mappings
        if persist and faiss_app.strip()=="":
            raise FileNotFoundError(f"Specify App name to use persistence.")
        self.faiss_storage = f"faiss_storage/{faiss_app}.bin"

        if not os.path.exists(self.faiss_storage):
            self.storage_exists = False
        self.model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    def store(self, file):


        document_vectors = \
            self.model.encode(documents, convert_to_numpy=True).astype('float32')

        index = None
        if self.persist:
            if self.storage_exists:
                index = self.read_index(self.faiss_storage)
            else:
                index = faiss.IndexFlatL2(d)
            pass
    pass
