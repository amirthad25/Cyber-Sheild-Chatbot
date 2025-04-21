from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    user_message: str

# Define predefined responses for CyberShield tools
predefined_responses = {
    "What does the Phishing URL Detector do?": "The Phishing URL Detector analyzes URLs to check if they are fraudulent or legitimate, helping users avoid phishing scams.",
    "How can I check my password strength?": "The Password Strength Checker evaluates your password and provides feedback on its security level, suggesting improvements if needed.",
    "What is the Network Security Scanner?": "The Network Security Scanner scans your network for vulnerabilities, helping you identify potential security risks.",
    "How does the Cyber Harassment Detector work?": "The Cyber Harassment Detector uses NLP to analyze messages and detect harmful or offensive content.",
    "Can I scan files for malware?": "Yes! The Malware File Scanner checks uploaded files for potential malware or viruses.",
    "What is Dark Web Monitoring?": "Dark Web Monitoring scans hidden web sources to check if your personal data has been leaked.",
    "How do I use the Phishing Detector?": "Simply enter a URL into the Phishing Detector tool, and it will analyze whether the link is safe or a phishing attempt.",
    "How can I report cyber harassment?": "If you experience cyber harassment, our tool provides guidance on reporting it to authorities and taking necessary actions.",
    "How does the chatbot help me with cybersecurity?": "The chatbot helps answer your questions about CyberShield's tools and provides cybersecurity tips.",
    "How can I create a strong password?": "Use a mix of uppercase, lowercase, numbers, and special characters to create a strong password. Avoid common words and phrases."
}

@app.post("/chat")
def chatbot_response(chat_request: ChatRequest):
    user_message = chat_request.user_message.strip()
    
    # Check if the question matches predefined responses
    response = predefined_responses.get(user_message, "Sorry, I don't have information on that. Please ask about CyberShield tools.")
    
    return {"response": response}
