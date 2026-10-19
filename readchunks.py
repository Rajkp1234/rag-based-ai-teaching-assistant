
import requests
import os
import json
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import joblib

def create_embedding(text_list):
    # https://github.com/ollama/ollama/blob/main/docs/api.md#generate-embeddings
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": text_list
    })

    embedding = r.json()["embeddings"]
    return embedding


json_folder = r"D:\2025 video\jsons"
jsons = os.listdir(json_folder)
my_dicts = []
chunk_id = 0

for json_file in jsons:
    with open(os.path.join(json_folder, json_file), encoding="utf-8") as f:
        content = json.load(f)

    print(f"Creating Embeddings for {json_file}")
    embeddings = create_embedding([c['text'] for c in content['chunks']])

    for i, chunk in enumerate(content['chunks']):
        chunk['chunk_id'] = chunk_id
        chunk['embedding'] = embeddings[i]
        chunk_id += 1
        my_dicts.append(chunk)

df = pd.DataFrame.from_records(my_dicts)

joblib.dump(df, r"D:\2025 video\embeddings.joblib")
