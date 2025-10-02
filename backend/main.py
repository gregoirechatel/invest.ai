from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Servir les fichiers statiques
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurer les templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("chemin.html", {"request": request})

@app.get("/etape1", response_class=HTMLResponse)
async def etape1(request: Request):
    return templates.TemplateResponse("1.html", {"request": request})

@app.get("/etape3", response_class=HTMLResponse)
async def etape3(request: Request):
    return templates.TemplateResponse("3.html", {"request": request})

# Étapes restantes -> placeholders
for i in list(range(2, 21)):
    if i not in (1, 3):
        async def placeholder(request: Request, step=i):
            return HTMLResponse(f"<h1>Page Étape {step} en construction...</h1>")
        app.add_api_route(f"/etape{i}", placeholder, methods=["GET"])
