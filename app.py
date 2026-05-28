import streamlit as st

# Import UI modules
from src.chatbot.ui import render_chatbot_ui
from src.resume_screening.ui import render_resume_screening_ui
from src.analytics.ui import render_analytics_ui


# ---------------------------------------------------
# Streamlit Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="AI Assistant Platform",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------------------------------
# Sidebar Navigation
# ---------------------------------------------------
st.sidebar.title("AI Assistant Platform")

page = st.sidebar.radio(
    "Select Module",
    [
        "AI Chatbot",
        "Resume Screening",
        "Analytics Dashboard"
    ]
)

# ---------------------------------------------------
# Route Pages
# ---------------------------------------------------
if page == "AI Chatbot":
    render_chatbot_ui()

elif page == "Resume Screening":
    render_resume_screening_ui()

elif page == "Analytics Dashboard":
    render_analytics_ui()