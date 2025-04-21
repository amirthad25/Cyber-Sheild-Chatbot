The CyberShield API is designed to assist users in obtaining information about cybersecurity tools provided by CyberShield. It answers questions about various tools, such as Phishing URL Detector, Password Strength Checker, Network Security Scanner, and more. This API is built using FastAPI and serves as a backend for interacting with users through a chatbot interface.

🚀 Features
Chatbot Integration: Users can send a message (via GET or POST request), and the API will return predefined responses related to CyberShield tools.

Predefined Responses: The API includes a set of predefined responses that provide detailed information about each CyberShield tool.

User-friendly: The API is simple to integrate with various interfaces (e.g., web, mobile) for a seamless user experience.

🧑‍💻 API Endpoints
POST /chat
This endpoint allows the user to send a message and receive a response based on the predefined answers related to CyberShield tools.

Request:
Method: POST

Payload:
{
  "user_message": "What does the Phishing URL Detector do?"
}
Response:
Success: Returns a predefined response based on the user's message.
{
  "response": "The Phishing URL Detector analyzes URLs to check if they are fraudulent or legitimate, helping users avoid phishing scams."
}
Default: If no matching response is found, the API will provide a default response.
{
  "response": "Sorry, I don't have information on that. Please ask about CyberShield tools."
}
🛠️ How to Use
Install FastAPI and Uvicorn:
pip install fastapi uvicorn

Run the API:
uvicorn cybershield:app --reload

Test the Endpoint:
You can use tools like Postman or Curl to test the API by sending a POST request with the user_message in the body.

Example using curl:
curl -X 'POST' \
'http://127.0.0.1:8000/chat' \
-H 'Content-Type: application/json' \
-d '{
    "user_message": "How can I check my password strength?"
}'
Response:

json
Copy
Edit
{
    "response": "The Password Strength Checker evaluates your password and provides feedback on its security level, suggesting improvements if needed."
}


💡 How It Works
ChatRequest Model: The API receives user messages as input in the form of a POST request. It uses the ChatRequest model to define the structure of the incoming request, which expects the user's message as a string.
Predefined Responses: The API matches the user’s input with predefined questions about CyberShield tools. If there is a match, it returns the corresponding answer. If no match is found, it returns a default response indicating that more information is needed.

🌐 Future Enhancements
Expand Responses: More cybersecurity topics and tools can be added to the predefined responses.
Integrate with NLP Models: Enhance the bot's ability to handle a broader range of user queries, improving its flexibility and usability.
User Authentication: Add user authentication to customize responses based on user preferences or previous interactions.
