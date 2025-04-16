from backend.rag_reindex import build_vector_database, load_markdown_files


def create_models(metadata_filename, bm25_filename, faiss_filename):
    print("Loading and indexing markdown documents...")
    documents = load_markdown_files()
    index, bm25, metadata = build_vector_database(documents, metadata_filename, bm25_filename, faiss_filename) 
    return index, bm25, metadata
