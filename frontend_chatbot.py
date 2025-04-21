import streamlit as st
import requests

# Streamlit UI setup
st.set_page_config(page_title="CyberShield Chatbot", layout="wide")

st.title("🤖 CyberShield Chatbot")
st.write("Ask me anything about CyberShield tools!")

# Chat input box
user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input:
        # Send user input to FastAPI backend
        response = requests.post("http://127.0.0.1:8000/chat", json={"user_message": user_input})
        
        if response.status_code == 200:
            chatbot_reply = response.json().get("response", "No response received.")
            st.text_area("Chatbot:", chatbot_reply, height=100)
        else:
            st.error("Failed to connect to chatbot API.")
