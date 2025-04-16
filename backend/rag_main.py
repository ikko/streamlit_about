from backend.rag_base import rag_load_or_create, rag_loop

if __name__ == "__main__":
    index, bm25, metadata = rag_load_or_create()
    print("here we are")
    rag_loop(index, bm25, metadata)
