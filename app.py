import streamlit as st

st.set_page_config(
    page_title="AI Assistant Platform",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Assistant Platform")

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Module",
    [
        "AI Chatbot",
        "Resume Screening",
        "Analytics Dashboard"
    ]
)

st.write(f"Current Module: {page}")