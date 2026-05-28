import streamlit as st
from datetime import datetime

from src.chatbot.chat_handler import get_ai_response


def render_chatbot_ui():

    st.title("🤖 AI Chatbot")

    st.markdown("---")

    # -----------------------------
    # Initialize Session State
    # -----------------------------
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # -----------------------------
    # Sidebar Controls
    # -----------------------------
    with st.sidebar:

        st.subheader("Chat Controls")

        if st.button("🗑️ Clear Chat"):

            st.session_state.messages = []
            st.rerun()

    # -----------------------------
    # Display Chat History
    # -----------------------------
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

            st.caption(message["time"])

    # -----------------------------
    # User Chat Input
    # -----------------------------
    user_input = st.chat_input("Type your message here...")

    if user_input:

        current_time = datetime.now().strftime("%H:%M:%S")

        # Store user message
        st.session_state.messages.append({
            "role": "user",
            "content": user_input,
            "time": current_time
        })

        # Generate AI response
        with st.spinner("AI is thinking..."):
            ai_response = get_ai_response(user_input)


        # Store assistant response
        st.session_state.messages.append({
            "role": "assistant",
            "content": ai_response,
            "time": current_time
        })

        st.rerun()