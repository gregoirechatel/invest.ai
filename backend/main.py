from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from backend.ai_engine import interpret_prompt

from backend.rules import parse_prompt_to_spec
from backend.calc import compute_mechanics

app = FastAPI(title="MechaMind PulleyGen v0.1")

# Config template system
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class PromptIn(BaseModel):
    text: str

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/design")
def design_from_prompt(data: PromptIn):
    spec = parse_prompt_to_spec(data.text)
    return spec

@app.post("/calc")
def calc_from_prompt(data: PromptIn):
    spec = parse_prompt_to_spec(data.text)
    result = compute_mechanics(spec)
    return {"spec": spec, "calculs": result}
@app.post("/ia")
def ia_from_prompt(data: PromptIn):
    result = interpret_prompt(data.text)
    return result
