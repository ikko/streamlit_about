import os

from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# OpenAI API key setup
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)
seed = 2025

# filenames of indexes and data
log_filename = Path("rag_openai.log")
metadata_filename = Path("rag_openai_metadata.json")
bm25_filename = Path("rag_bm25result.pickle")
faiss_filename = Path("rag_openai_faiss.index")
