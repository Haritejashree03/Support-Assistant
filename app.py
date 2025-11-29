import streamlit as st
from agent.rag_pipeline import answer_query
from agent.db import log_ticket

st.set_page_config(page_title="Support Assistant", page_icon="🤖", layout="centered")

st.title("🤖 Support Assistant Agent")
st.write("Ask any support-related question and I’ll try my best to help!")

query = st.text_input("Enter your question:")

if st.button("Ask"):
    if query.strip() == "":
        st.warning("Please type a question.")
    else:
        response, confidence = answer_query(query)

        st.write("### Response:")
        st.write(response)
        st.caption(f"Confidence score: {confidence:.2f}")

        # UI indicators
        if "Here is what I found online" in response:
            st.info("🌎 Found information using Internet Search")
        elif "human support" in response.lower():
            st.error("⚠ Escalated to Human Support")
            log_ticket(query, "Pending", confidence)
        elif "summarized answer from the Internet" in response:
            st.info("🌎 Answered using Internet Search")
        else:
            st.success("Answered from Internal Knowledge Base")
