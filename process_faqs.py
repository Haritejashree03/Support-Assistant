import json
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def process_faqs():
    with open("data/faqs.json", "r", encoding="utf-8") as f:
        faqs = json.load(f)

    processed = []
    for item in faqs:
        combined_text = item["question"] + " " + item["answer"]
        emb = model.encode(combined_text).tolist()

        processed.append({
            "question": item["question"],
            "answer": item["answer"],
            "embedding": emb
        })

    with open("data/faqs_processed.json", "w", encoding="utf-8") as f:
        json.dump(processed, f, indent=4)

    print("🎉 Embeddings generated successfully → faqs_processed.json created.")

if __name__ == "__main__":
    process_faqs()
