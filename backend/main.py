from fastapi import FastAPI
from pydantic import BaseModel
from backend.rules import parse_prompt_to_spec, Spec
from backend.calc import compute_mechanics


app = FastAPI(title="MechaMind PulleyGen v0.1")

class PromptIn(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Bienvenue sur MechaMind PulleyGen v0.1 🚀"}

@app.post("/design")
def design_from_prompt(data: PromptIn):
    spec = parse_prompt_to_spec(data.text)
    return spec

@app.post("/calc")
def calc_from_prompt(data: PromptIn):
    spec = parse_prompt_to_spec(data.text)
    result = compute_mechanics(spec)
    return {"spec": spec, "calculs": result}
