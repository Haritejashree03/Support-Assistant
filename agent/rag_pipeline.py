import json
import numpy as np
from sentence_transformers import SentenceTransformer, util
from agent.web_search import internet_search
from agent.summarizer import summarize_text  # <-- new Summarizer import

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load processed FAQ data
with open("data/faqs_processed.json", "r", encoding="utf-8") as f:
    faq_data = json.load(f)

# Embedding vectors
embeddings = np.array([np.array(item["embedding"], dtype=np.float32) for item in faq_data])

def get_embedding(text):
    return model.encode(text, convert_to_numpy=True).astype(np.float32)

def retrieve_relevant_context(query):
    query_emb = get_embedding(query)
    similarity = util.cos_sim(query_emb, embeddings)[0]
    top_idx = int(similarity.argmax())
    score = float(similarity[top_idx])

    best_question = faq_data[top_idx]["question"]
    best_answer = faq_data[top_idx]["answer"]

    return best_question, best_answer, score

def answer_query(query, threshold: float = 0.60):
    """
    Returns:
    - Internal FAQ answer if score high enough
    - Internet summarized answer if FAQ match weak
    - Escalation if no info found
    """
    best_question, best_answer, score = retrieve_relevant_context(query)

    # Condition 1 — Answer confidently from knowledge base
    if score >= threshold:
        return best_answer, score

    # Condition 2 — Attempt internet search fallback
    web_data = internet_search(query)
    if web_data:
        return (
            f"I could not find this in our internal knowledge base.\n\n"
            f"Here is what I found online:\n\n{web_data}",score
            )
    
    # Condition 3 — escalate if both fail
    return "I need help from a human support agent.", score