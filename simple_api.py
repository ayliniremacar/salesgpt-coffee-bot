import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

class MessageList(BaseModel):
    session_id: str
    human_say: str

@app.get("/")
async def say_hello():
    return {"message": "Coffee Bot API is running!"}

@app.get("/botname")
async def get_bot_name():
    return {"name": "Kahve Uzmanı", "model": "gpt-3.5-turbo"}

@app.post("/chat")
async def chat_with_sales_agent(req: MessageList):
    # Basit test yanıtı
    return {
        "bot_name": "Kahve Uzmanı",
        "conversational_stage": "Introduction",
        "response": f"Merhaba! Ben Kahve Uzmanı. '{req.human_say}' mesajınızı aldım. Şu anda test modundayız.",
        "thinking_process": {
            "conversationalStage": "Introduction",
            "useTools": False
        }
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port) 