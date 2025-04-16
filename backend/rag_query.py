import os
import html
import json
from datetime import datetime
from time import sleep

import numpy as np

from backend.rag_config import client, log_filename
from backend.rag_reindex import get_embedding
from backend.timer_util import timer
from backend.email_send import send_message

# Hybrid search: BM25 + FAISS
@timer
def query_rag(question, index, bm25, metadata, session_id=None, top_k=8):
    question_embeddings = get_embedding(question)
    faiss_indices = query_faiss(index, question_embeddings, top_k)
    bm25_indices = query_bm25(bm25, question, top_k)
    retrieved_texts = query_hybrid(bm25_indices, faiss_indices, metadata)
    context = "\n".join(retrieved_texts)
    full_response = yield from call_completions_api(context, question)
    log_query_and_answer(full_response, question)
    return full_response


def log_query_and_answer(full_response, question):
    to_be_logged = {
        "timestamp": datetime.now().isoformat(),
        "query": question,
        "response": full_response,
    }
    email_subject = f"streamlit RAG Q: {question}"
    email_body_json = json.dumps(to_be_logged, indent=4)
    escaped_json = html.escape(email_body_json, quote=True)
    html_output = f"<pre>{escaped_json}</pre>"
    send_message(subject=email_subject, body=html_output)


def call_completions_api(context, question):
    prompt = (f"Answer based on the following information, the context:\n\n{context}\n\nQuestion"
              f":{question}\nAnswer:")
    messages = [
        {"role": "system", "content": os.getenv("SYSTEM_PROMPT")},
        {"role": "user", "content": prompt}
    ]
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        stream=True
    )
    print("\n💡 RAG answer:\n", end="")
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content:
            text = chunk.choices[0].delta.content
            full_response += text
            print(text, end="", flush=True)
        yield chunk
    return full_response


@timer
def query_faiss(index, question_embeddings, top_k):
    question_embedding_np = np.array(question_embeddings).astype("float32").reshape(1, -1)
    _, faiss_indices = index.search(question_embedding_np, top_k)
    return faiss_indices


@timer
def query_bm25(bm25, question, top_k):
    tokenized_question = question.split()
    bm25_scores = bm25.get_scores(tokenized_question)
    bm25_indices = np.argsort(bm25_scores)[-top_k:][::-1]
    return bm25_indices


@timer
def query_hybrid(bm25_indices, faiss_indices, metadata):
    combined_indices = list(set(faiss_indices[0]) | set(bm25_indices))
    retrieved_texts = [metadata[i][1] for i in combined_indices]
    hybrid_context = '\n'.join(retrieved_texts)
    return retrieved_texts
