from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / ".env"
print(f"🔍 Loading .env from: {env_path}")
load_dotenv(dotenv_path=env_path)

#from backend.mock_model import MockModel
from mock_model import MockModel



app = FastAPI()


# ✅ Load your model (mock version)
model = MockModel()

# ✅ Pydantic schema
class PromptRequest(BaseModel):
    prompt: str

# ✅ API route
@app.post("/generate")
async def generate_text(request: PromptRequest):
    response = model.generate(request.prompt)
    return {"response": response}
