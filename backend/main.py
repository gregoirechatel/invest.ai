from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Servir les fichiers statiques (CSS, images…)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurer les templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("chemin.html", {"request": request})

# Créer 20 routes (une par étape, elles renverront vers de futures pages)
for i in range(1, 21):
    async def placeholder(request: Request, step=i):
        return HTMLResponse(f"<h1>Page Étape {step} en construction...</h1>")
    app.add_api_route(f"/etape{i}", placeholder, methods=["GET"])
