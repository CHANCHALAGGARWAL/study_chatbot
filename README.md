Study Bot 🤖

An AI-powered educational chatbot built using FastAPI, LangChain, MongoDB Atlas, and Groq LLM. The application helps users ask study-related questions and receive intelligent responses while maintaining conversation history.

🚀 Features
AI-powered question answering
Conversation history storage
FastAPI REST API
MongoDB Atlas integration
LangChain-powered workflow
Groq LLM support
Cloud deployment on Render
🛠️ Tech Stack
Python
FastAPI
MongoDB Atlas
LangChain
Groq API
Render
📌 API Endpoints
Home Endpoint

GET /

Returns API status and available endpoints.

Chat Endpoint

POST /chat

Request Example:

{
"user_id": "student1",
"question": "What is Django?"
}

Response Example:

{
"response": "Django is a high-level Python web framework..."
}

🌐 Live Demo

https://study-chatbot-lw97.onrender.com

📖 API Documentation

https://study-chatbot-lw97.onrender.com/docs

⚙️ Installation
Clone the repository
Install dependencies using requirements.txt
Configure environment variables
Run the FastAPI application
🔑 Environment Variables

Create a .env file and add:

GROQ_API_KEY=your_groq_api_key

MONGODB_URI=your_mongodb_connection_string

👩‍💻 Author

Chanchal Aggarwal

B.Tech Computer Science & Engineering

📄 License

This project is intended for educational and learning purposes.
