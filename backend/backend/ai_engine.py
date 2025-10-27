import os


OPENROUTER_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = "anthropic/claude-3-haiku"  # ou "openai/gpt-4o-mini"

def interpret_prompt(prompt: str) -> dict:
    """
    Envoie le texte utilisateur à OpenRouter et récupère
    un JSON structuré décrivant la conception mécanique.
    """
    if not OPENROUTER_KEY:
        raise ValueError("Clé OpenRouter manquante sur Render")

    headers = {
        "Authorization": f"Bearer {OPENROUTER_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": (
                "Tu es un ingénieur mécanique expert. "
                "Analyse les besoins exprimés et fournis un JSON structuré avec ces clés : "
                "type (chape ou porte-a-faux), load_mass_kg, duty_hours, material, "
                "diameter_mm, rope_diameter_mm, commentaire."
            )},
            {"role": "user", "content": prompt}
        ]
    }

    r =.post("https://openrouter.ai/api/v1/chat/completions",
                      headers=headers, json=data)

    if r.status_code != 200:
        raise RuntimeError(f"Erreur API OpenRouter: {r.text}")

    content = r.json()["choices"][0]["message"]["content"]

    # Essaye d’extraire un JSON, sinon renvoie texte brut
    import json, re
    try:
        json_str = re.search(r"\{.*\}", content, re.S).group()
        return json.loads(json_str)
    except Exception:
        return {"reponse_brute": content}
