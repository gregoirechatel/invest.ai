from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="MechaMind PulleyGen v0.1")

class PromptIn(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Bienvenue sur MechaMind PulleyGen v0.1 🚀"}

@app.post("/design")
def design_from_prompt(data: PromptIn):
    return {"message": f"Prompt reçu : {data.text}"}
