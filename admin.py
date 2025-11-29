import streamlit as st
import pandas as pd

st.set_page_config(page_title="Admin Ticket Dashboard", page_icon="📑", layout="wide")

st.title("📑 Support Assistant – Admin Panel")
st.write("All escalated customer queries:")

try:
    df = pd.read_csv("tickets.csv", header=None)
    df.columns = ["Timestamp", "Query", "Status", "Confidence"]

    st.dataframe(df, use_container_width=True)

    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="⬇ Download Tickets CSV",
        data=csv,
        file_name="tickets_export.csv",
        mime="text/csv"
    )

except FileNotFoundError:
    st.warning("No escalated tickets found yet. Ticket file will appear when escalation happens.")
