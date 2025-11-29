from duckduckgo_search import DDGS

def internet_search(query, max_results=10):
    """
    Performs focused DuckDuckGo search and extracts most relevant result.
    """
    try:
        enriched_query = f"{query} accurate answer price India facts definition meaning explained summary"

        with DDGS() as ddgs:
            results = ddgs.text(enriched_query, max_results=max_results)

        candidate_sentences = []

        for r in results:
            title = r.get("title", "")
            body = r.get("body", "")
            text = f"{title}. {body}".strip()

            key_phrases = ["price", "₹", "inr", "rs", "is", "are", "was", "founded", "meaning", "definition"]
            if any(word in text.lower() for word in key_phrases):
                candidate_sentences.append(text)

        # return best filtered result
        if candidate_sentences:
            return candidate_sentences[0]  # MOST relevant answer

        return None
    except Exception as e:
        print("internet search error:", e)
        return None
