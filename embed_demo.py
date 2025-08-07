
import os
from typing import List
from mistralai.client import MistralClient
from sentence_transformers.util import cos_sim

import json
import os
import pickle
from pathlib import Path
from typing import Dict, List, Tuple, Set, Optional, Any
import numpy as np
from tqdm import tqdm
from datasets import load_dataset
from mistralai import Mistral
from langchain.text_splitter import Language, RecursiveCharacterTextSplitter
import faiss
from collections import defaultdict
import re
from getpass import getpass

from huggingface_hub import hf_hub_download
from mistral_common.tokens.tokenizers.tekken import Tekkenizer

api_key = getpass("Enter your MISTRAL_API_KEY: ").strip()
os.environ["MISTRAL_API_KEY"] = api_key


client = Mistral(api_key=api_key.strip())

EMBED_MODEL = "codestral-embed"

def read_files(file_paths: List[str]) -> List[str]:
    return [open(path, "r", encoding="utf-8").read() for path in file_paths]

def embed_texts(texts: List[str]) -> List[List[float]]:
    response = client.embeddings.create(
                model=EMBED_MODEL,
                inputs=texts,
            )
    return [item.embedding for item in response.data]

def retrieve_top_k(file_contents: List[str], file_names: List[str], query: str, k: int = 1):
    embeddings = embed_texts(file_contents + [query])
    file_embeddings = embeddings[:-1]
    query_embedding = embeddings[-1]

    scores = cos_sim(query_embedding, file_embeddings)[0]
    indexed_scores = list(enumerate(scores))
    sorted_scores = sorted(indexed_scores, key=lambda x: x[1], reverse=True)

    results = [(file_names[i], score.item()) for i, score in sorted_scores]
    return results[:k], results  # return both top_k and all scores

if __name__ == "__main__":
    input_str = input("Enter all file names (comma-separated): ").strip()
    file_paths = [f.strip() for f in input_str.split(',') if f.strip()]
    file_names = [os.path.basename(p) for p in file_paths]
    file_contents = read_files(file_paths)

    problem_statement = input("Enter the problem statement: ").strip()
    top_k, all_scores = retrieve_top_k(file_contents, file_names, problem_statement, k=1)

    print("All file similarity scores:")
    for fname, score in all_scores:
        print(f"{fname}: {score:.4f}")

    print("\nTop match:")
    for fname, score in top_k:
        print(f"{fname} (Score: {score:.4f})")

