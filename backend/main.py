from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import Model

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="frontend")

# Setup IBM Granite
creds = Credentials(api_key="h7cMpyUJXyGbHi3FBmj7okzysDHEGTAuhHty7kqeWyb_", url="https://us-south.ml.cloud.ibm.com")
model = Model("ibm-granite/granite-3.3-2b-instruct", creds)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict_disease")
async def predict_disease(symptoms: str = Form(...)):
    prompt = f"A patient has the following symptoms: {symptoms}. What could be the most likely diseases?"
    result = model.generate_text(prompt)
    return {"response": result}

@app.post("/home_remedy")
async def home_remedy(disease: str = Form(...)):
    prompt = f"Suggest a natural home remedy for the disease: {disease}."
    result = model.generate_text(prompt)
    return {"response": result}
