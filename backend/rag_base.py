from backend.rag_config import bm25_filename, faiss_filename, metadata_filename
from backend.rag_models_create import create_models
from backend.rag_models_load import load_models
from backend.rag_query import query_rag
from backend.timer_util import timer


@timer
def rag_load_or_create():
    # If the metadata exists, we load the indexes otherwise we create the models 
    if metadata_filename.exists() and bm25_filename.exists() and faiss_filename.exists():
        index, bm25, metadata = load_models(metadata_filename, bm25_filename, faiss_filename)
    else:
        index, bm25, metadata = create_models(metadata_filename, bm25_filename, faiss_filename)
    return index, bm25, metadata

def rag_loop(index, bm25, metadata):
    print("✅ RAG system ready!")
    while True:
        print("✅ in the loop!")
        query = input("Your question (or 'exit' to quit): ")
        if query.lower() == "exit":
            break
        query_rag(query, index, bm25, metadata)

