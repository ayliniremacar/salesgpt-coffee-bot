import json
import os
from typing import List, Optional

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Query, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel

# Load environment variables
load_dotenv()

# Initialize FastAPI app
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

# Kahve ürün kataloğu
COFFEE_PRODUCTS = {
    "espresso_machines": [
        {
            "name": "DeLonghi ECAM 370.95.T Dinamica Plus",
            "price": "12.999 TL",
            "water_capacity": "1.8L",
            "warranty": "2 yıl",
            "stock": "Mevcut",
            "features": "Otomatik espresso makinesi, 13 kahve seviyesi, süt köpürtücü, dijital ekran"
        },
        {
            "name": "Breville BES870XL Barista Express",
            "price": "8.499 TL",
            "water_capacity": "2L",
            "warranty": "2 yıl",
            "stock": "Mevcut",
            "features": "Manuel espresso makinesi, entegre kahve değirmeni, süt köpürtücü"
        }
    ],
    "filter_machines": [
        {
            "name": "Moccamaster KBG Select",
            "price": "3.899 TL",
            "water_capacity": "1.25L",
            "warranty": "5 yıl",
            "stock": "Mevcut",
            "features": "Manuel filtre kahve makinesi, 3 sıcaklık seviyesi"
        }
    ],
    "capsule_machines": [
        {
            "name": "Nespresso Vertuo Plus",
            "price": "2.999 TL",
            "water_capacity": "1.5L",
            "warranty": "2 yıl",
            "stock": "Mevcut",
            "features": "Kapsül kahve makinesi, 5 farklı kapsül boyutu"
        }
    ]
}

# Basit AI yanıt sistemi
def get_ai_response(user_message: str) -> str:
    user_message = user_message.lower()
    
    # Su kapasitesi sorguları
    if "su kapasitesi" in user_message or "kapasite" in user_message:
        if "delonghi" in user_message:
            return "DeLonghi ECAM 370.95.T Dinamica Plus modelinin su kapasitesi 1.8L'dir."
        elif "breville" in user_message:
            return "Breville BES870XL Barista Express modelinin su kapasitesi 2L'dir."
        elif "nespresso" in user_message:
            return "Nespresso Vertuo Plus modelinin su kapasitesi 1.5L'dir."
        else:
            return "Espresso makinelerimizin su kapasiteleri: DeLonghi 1.8L, Breville 2L, Nespresso 1.5L'dir."
    
    # Stok sorguları
    elif "stok" in user_message or "mevcut" in user_message:
        return "Tüm ürünlerimiz şu anda stokta mevcuttur. DeLonghi, Breville, Nespresso ve Moccamaster modellerimizi inceleyebilirsiniz."
    
    # Garanti sorguları
    elif "garanti" in user_message:
        return "Espresso makinelerimiz 2 yıl, filtre kahve makinelerimiz 5 yıl garanti kapsamındadır. Ayrıca 14 gün içinde iade garantisi sunuyoruz."
    
    # Fiyat sorguları
    elif "fiyat" in user_message or "kaç para" in user_message:
        return "Fiyatlarımız: DeLonghi 12.999 TL, Breville 8.499 TL, Nespresso 2.999 TL, Moccamaster 3.899 TL'dir."
    
    # Genel bilgi
    elif "merhaba" in user_message or "selam" in user_message:
        return "Merhaba! Ben Premium Kahve'nin Kahve Uzmanı. Size en uygun kahve makinesini bulmanızda yardımcı olabilirim. Hangi tür kahve makinesi arıyorsunuz?"
    
    # Varsayılan yanıt
    else:
        return "Kahve makinesi hakkında bilgi almak istiyorsanız, su kapasitesi, fiyat, garanti süresi veya stok durumu hakkında sorabilirsiniz."

@app.get("/")
async def say_hello():
    return JSONResponse(
        content={"message": "Premium Kahve Bot API is running!"},
        media_type="application/json; charset=utf-8"
    )

@app.get("/botname")
async def get_bot_name():
    return JSONResponse(
        content={"name": "Kahve Uzmanı", "model": "Coffee Expert v1.0"},
        media_type="application/json; charset=utf-8"
    )

@app.post("/chat")
async def chat_with_sales_agent(req: MessageList):
    ai_response = get_ai_response(req.human_say)
    
    return JSONResponse(
        content={
            "bot_name": "Kahve Uzmanı",
            "conversational_stage": "Information",
            "response": ai_response,
            "thinking_process": {
                "conversationalStage": "Information",
                "useTools": False
            }
        },
        media_type="application/json; charset=utf-8"
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port) 