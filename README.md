# RAG-Based AI Teaching Assistant

## Overview
RAG-Based AI Teaching Assistant is a Python project designed to answer questions about educational videos and learning materials. It uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from video transcripts and generate context-based answers.

The project can be adapted to different types of educational content, including lectures, tutorials, and recorded lessons, provided their transcripts are available.

## Features
- Processes video transcripts into manageable text chunks.
- Generates text embeddings using Ollama and the `bge-m3` model.
- Retrieves relevant content using cosine similarity.
- Generates answers using the `qwen3:0.6b` language model.
- Uses retrieved transcript content to provide context-aware answers.
- Includes relevant video titles and timestamps when available.
- Can be extended to support different educational subjects and learning materials.

## Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Requests
- Ollama
- bge-m3
- qwen3:0.6b

## How It Works
1. Process transcripts from educational videos.
2. Split transcript text into smaller chunks.
3. Generate embeddings for the chunks.
4. Convert the user's question into an embedding.
5. Retrieve the most relevant chunks using cosine similarity.
6. Provide the retrieved context and question to the language model.
7. Generate an answer based on the available context.

## Requirements
- Python installed
- Ollama installed and running
- `bge-m3` embedding model
- `qwen3:0.6b` language model

## Future Improvements
- Support multiple educational subjects and courses.
- Add PDF and document-based question answering.
- Build a web interface for students.
- Improve retrieval accuracy and answer evaluation.

## Project Status
This is a learning project under development. Its answer quality depends on transcript quality, retrieval accuracy, and the language model.

## Author
Raj Kumar