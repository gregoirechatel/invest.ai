from pydantic import BaseModel
from typing import Literal, Optional
import re

# Types possibles
PulleyType = Literal["chape", "porte-a-faux"]
Material = Literal["S235", "S355", "42CrMo4", "Al-6082", "PA6"]

# Modèle de spécifications
class Spec(BaseModel):
    type: PulleyType = "porte-a-faux"
    load_mass_kg: float = 100.0
    duty_hours: float = 1.0
    material: Material = "S355"
    diameter_mm: float = 120.0
    rope_diameter_mm: float = 10.0

def parse_prompt_to_spec(prompt: str) -> Spec:
    text = prompt.lower()
    spec = Spec()

    # Type de poulie
    if "chape" in text:
        spec.type = "chape"
    if "porte" in text and "faux" in text:
        spec.type = "porte-a-faux"

    # Charge (kg)
    m = re.search(r"(\\d+[\\.,]?\\d*)\\s*kg", text)
    if m:
        spec.load_mass_kg = float(m.group(1).replace(",", "."))

    # Durée (heures)
    h = re.search(r"(\\d+[\\.,]?\\d*)\\s*heures?", text)
    if h:
        spec.duty_hours = float(h.group(1).replace(",", "."))

    # Matériau
    if "s235" in text: spec.material = "S235"
    if "s355" in text: spec.material = "S355"
    if "42crmo4" in text: spec.material = "42CrMo4"
    if "alu" in text or "aluminium" in text: spec.material = "Al-6082"
    if "pa6" in text or "nylon" in text: spec.material = "PA6"

    # Diamètre
    d = re.search(r"(\\d+[\\.,]?\\d*)\\s*mm", text)
    if d:
        spec.diameter_mm = float(d.group(1).replace(",", "."))

    return spec
