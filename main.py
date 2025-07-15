from fastapi import FastAPI, Request
import chromadb
from chromadb.config import Settings
import requests
import os

# Inicializa ChromaDB client local
chroma_client = chromadb.PersistentClient(
    path="/data/chroma"
)
# Usa una colección única para los README (puedes cambiar el nombre)
collection = chroma_client.get_or_create_collection("readmes")

app = FastAPI()

@app.post("/ingest-readme")
async def ingest_readme(payload: dict):
    """
    Descarga y vectoriza el README de un repo de GitHub.
    Ejemplo body: { "repo": "ai-agent" }
    """
    repo = payload.get("repo")
    if not repo:
        return {"error": "Falta 'repo'"}
    url = f"https://raw.githubusercontent.com/dorado-ai-devops/{repo}/main/README_ES.md"
    resp = requests.get(url)
    if resp.status_code != 200:
        return {"error": f"No se pudo obtener README de {repo}: {resp.status_code}"}
    text = resp.text
    # Guarda y vectoriza (id único = repo)
    collection.add(
        documents=[text],
        ids=[repo],
        metadatas=[{"repo": repo}]
    )
    return {"ok": True, "repo": repo, "chars": len(text)}

@app.post("/query")
async def query_vector_db(payload: dict):
    """
    Busca por similitud en los vectores de los README.
    Ejemplo body: { "query": "¿Cómo funciona el pipeline de logs?" }
    """
    query = payload.get("query")
    if not query:
        return {"error": "Falta 'query'"}
    res = collection.query(query_texts=[query], n_results=3)
    # Devuelve los textos y metadatas más relevantes
    return {
        "results": [
            {"repo": md["repo"], "text": doc}
            for doc, md in zip(res["documents"][0], res["metadatas"][0])
        ]
    }

@app.get("/ping")
async def ping():
    return {"status": "ok"}

# Si quieres correr en local: uvicorn main:app --reload --host 0.0.0.0 --port 8888
