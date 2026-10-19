import pandas as pd 
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 
import joblib 
import requests


def create_embedding(text_list):
    # https://github.com/ollama/ollama/blob/main/docs/api.md#generate-embeddings
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": text_list
    })

    embedding = r.json()["embeddings"] 
    return embedding


def inference(prompt):
    r = requests.post("http://localhost:11434/api/generate", json={
        "model": "qwen3:0.6b",
        "prompt": prompt,
        "stream": False
    })

    response = r.json()
    print(response)
    return response


df = joblib.load(r"D:\2025 video\embeddings.joblib")


incoming_query = input("Ask a Question: ")
question_embedding = create_embedding([incoming_query])[0] 

# Find similarities of question_embedding with other embeddings
# print(np.vstack(df['embedding'].values))
# print(np.vstack(df['embedding']).shape)

similarities = cosine_similarity(
    np.vstack(df['embedding']), [question_embedding]
).flatten()

# print(similarities)

top_results = 5
max_indx = similarities.argsort()[::-1][0:top_results]

# print(max_indx)

new_df = df.iloc[max_indx] 

# print(new_df[["title", "number", "text"]])

prompt = f'''You are answering questions about a cartoon video.
Here are subtitle chunks containing video title, video number, start time, end time, and dialogue:

{new_df[["title", "number", "start", "end", "text"]].to_json(orient="records")}
---------------------------------
User question: "{incoming_query}"

Answer the user's question in a natural and simple way using only the provided video chunks.
Mention the relevant video title and timestamp when possible.
If the question is unrelated to the cartoon video or the information is not available in the provided chunks, say that you can only answer questions based on the available cartoon video content.
'''

with open(r"D:\2025 video\prompt.txt", "w", encoding="utf-8") as f:
    f.write(prompt)

response = inference(prompt)["response"]
print(response)

with open(r"D:\2025 video\response.txt", "w", encoding="utf-8") as f:
    f.write(response)

# for index, item in new_df.iterrows():
#     print(index, item["title"], item["number"], item["text"], item["start"], item["end"])