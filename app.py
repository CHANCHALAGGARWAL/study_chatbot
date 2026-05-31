import datetime
import os 
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from pymongo import MongoClient # type: ignore
from datetime import datetime
from fastapi import FastAPI # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore
from pydantic import BaseModel

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
mongo_uri= os.getenv("MONGODB_URI")

client = MongoClient(mongo_uri)
db = client["chatbot"]
collection = db["users"]

app = FastAPI()

class ChatRequest(BaseModel):
    user_id: str
    question: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "YOU ARE A STUDY BOT"),
        ("placeholder", "{history}"),
        ("user", "{question}")
    ]
)

llm = ChatGroq(api_key = groq_api_key, model = "openai/gpt-oss-20b")  # type: ignore
chain = prompt | llm

def get_history(user_id):
    chat = collection.find({"user_id": user_id}).sort("timestamp", 1)
    history = []
    
    for chatbot in chat:
        history.append((chatbot["role"],chatbot["message"]))
    return history

@app.get("/")
def home():
    return {
        "project": "Study Bot",
        "status": "Active",
        "docs": "/docs",
        "chat_endpoint": "/chat"
    }

@app.post("/chat")
def chat(request: ChatRequest):
    history = get_history(request.user_id)
    response = chain.invoke({"history":history, "question": request.question})
    
    collection.insert_one({
        "user_id": request.user_id,
        "role": "user",
        "message": request.question,
        "timestamp": datetime.utcnow()
    })
    
    collection.insert_one({
        "user_id": request.user_id,
        "role": "assistant",
        "message": response.content,
        "timestamp": datetime.utcnow()
    })
    
    return {"response": response.content}