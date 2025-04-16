import json
import pickle
import faiss

def load_models(metadata_filename, bm25_filename, faiss_filename):
    print("Loading existing models...")
    index = faiss.read_index(str(faiss_filename))
    with open(bm25_filename, "rb") as file:
        bm25 = pickle.load(file)
    with open(metadata_filename, "r", encoding="utf-8") as file:
        metadata = json.load(file)
    return index, bm25, metadata
