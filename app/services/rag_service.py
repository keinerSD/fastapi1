import faiss
import json
import numpy as np
import os
import re

from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from openai import OpenAI
from deep_translator import GoogleTranslator


load_dotenv()

print("Loading embedding model...")
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

print("Loading FAISS index...")
index = faiss.read_index("data/medical_index.faiss")

print("Loading dataset...")
with open("data/medical_diseases.json", "r", encoding="utf-8") as f:
    dataset = json.load(f)

print("Connecting to Groq...")
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

print("RAG system ready.")


# FUNCIÓN PRINCIPAL RAG

def medical_rag_query(query: str):

    # traducir síntomas a inglés
    query_en = GoogleTranslator(source="auto", target="en").translate(query)

    # embedding
    query_embedding = embedding_model.encode([query_en], normalize_embeddings=True)
    query_embedding = np.array(query_embedding).astype("float32")

    # búsqueda vectorial
    k = 10
    distances, indices = index.search(query_embedding, k)

    print("Query:", query_en)
    print("Distances:", distances)
    print("Indices:", indices)

    possible_diseases = []

    for dist, idx in zip(distances[0], indices[0]):

        disease = dataset[idx]["metadata"]["disease"]

        if disease not in possible_diseases:
            possible_diseases.append(disease)

        if len(possible_diseases) >= 3:
            break

    print("Possible diseases:", possible_diseases)

    context = ""
    count = 0
    MAX_CONTEXT_DOCS = 3

    for dist, idx in zip(distances[0], indices[0]):

        if dataset[idx]["metadata"]["section"] != "symptoms":
            continue

        if dist < 0.95 and count < MAX_CONTEXT_DOCS:
            context += dataset[idx]["text"] + "\n"
            count += 1

    print("Context:", context)

    best_distance = distances[0][0]

    print(best_distance)
    if best_distance > 1.1:
        return {
            "disease": None,
            "explanation": "Los síntomas no coinciden claramente con enfermedades del sistema.",
            "recommendation": "Consulte a un profesional de salud para una evaluación adecuada."
        }

    if best_distance < 0.8:
        confidence = "alta"

    elif best_distance < 0.95:
        confidence = "media"

    else:
        confidence = "baja"

    possible_diseases_json = json.dumps(possible_diseases)


    # prompt
    prompt = f"""
You are a strict medical extraction system.

Your task is to extract information ONLY from the provided medical context.

Medical context:
{context}

Possible diseases (from similarity search):
{possible_diseases}

User symptoms:
{query}

STRICT RULES:
- You MUST ONLY use information that appears explicitly in the medical context.
- DO NOT add any external medical knowledge.
- DO NOT infer or guess.
- If the context does not contain enough information, return:
"No puedo determinar la enfermedad con la información proporcionada."

- The explanation MUST be directly based on the context.
- The recommendation MUST be directly taken or derived ONLY from the context.
- If recommendation is not present in the context, write: "No disponible en la información."

OUTPUT RULES:
- Answer ONLY in Spanish.
- Return ONLY a valid JSON.
- Do NOT write text before or after the JSON.
- Do NOT explain anything outside the JSON.

FORMAT:

{{
"disease": "one disease from the list",
"possible_diseases": {possible_diseases_json},
"explanation": "based ONLY on context",
"recommendation": "based ONLY on context or 'No disponible en la información.'",
"confidence": "{confidence}"
}}
"""
    
    response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role": "user", "content": prompt}]
    )

    result = response.choices[0].message.content
    print(result)

# extraer solo el json
    match = re.search(r"\{.*?\}", result, re.DOTALL)

    if match:
        json_text = match.group()
        data = json.loads(json_text)
        return data
    
    return {
        "disease": None,
        "explanation": "No se pudo interpretar la respuesta del modelo.",
        "recommendation": "Intente nuevamente.",
    }

    


    
