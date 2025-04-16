import json
import os
import pickle
from pathlib import Path

import faiss
import numpy as np

import tiktoken
from rank_bm25 import BM25Okapi

from backend.rag_config import client


def load_markdown_files(directory="data"):
    documents = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    documents.append(f"{file_path}: {content}")                   
    return documents


def chunk_text(text, max_tokens=1024):
    tokenizer = tiktoken.get_encoding("cl100k_base")
    tokens = tokenizer.encode(text)
    chunks = [tokens[i: i + max_tokens] for i in range(0, len(tokens), max_tokens)]
    return [tokenizer.decode(chunk) for chunk in chunks]


def get_embedding(text, model="text-embedding-ada-002"):
    response = client.embeddings.create(input=text, model=model)
    return response.data[0].embedding


def build_vector_database(documents, metadata_filename: Path, bm25_filename: Path, faiss_filename: Path):
    index = faiss.IndexFlatL2(1536)
    vectors = []
    metadata = []
    tokenized_docs = []

    for doc_id, doc in enumerate(documents):
        chunks = chunk_text(doc)
        for chunk in chunks:
            embedding = get_embedding(chunk)
            vectors.append(embedding)
            metadata.append((doc_id, chunk))
            tokenized_docs.append(chunk.split())

    # Fill FAISS database
    vectors = np.array(vectors).astype("float32")
    index.add(vectors)

    # Build BM25 index
    bm25 = BM25Okapi(tokenized_docs)

    # Persist FAISS and BM25 models
    faiss.write_index(index, str(faiss_filename))
    with open(bm25_filename, "wb") as file:
        pickle.dump(bm25, file)
    with open(metadata_filename, "w", encoding="utf-8") as file:
        json.dump(metadata, file, ensure_ascii=False, indent=4)

    return index, bm25, metadata
