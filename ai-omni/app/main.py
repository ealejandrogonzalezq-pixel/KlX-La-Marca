from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import HTMLResponse
import os

app = FastAPI(title="KIX-La-Marca - AI-Omni")

# Crea carpetas si no existen
os.makedirs("uploads", exist_ok=True)

@app.get("/", response_class=HTMLResponse)
async def home():
    # Intenta leer el index.html en 2 lugares posibles
    paths = ["ai-omni/static/index.html", "static/index.html"]
    for p in paths:
        if os.path.exists(p):
            with open(p, "r", encoding="utf-8") as f:
                return f.read()
    return """
    <h1>🚀 KIX-La-Marca AI-Omni funcionando</h1>
    <p>El servidor está vivo. Ahora crea el archivo ai-omni/static/index.html</p>
    """

@app.post("/ask")
async def ask_question(question: str = Form(...)):
    return {
        "respuesta": f"🤖 KIX AI-Omni investigando: '{question}'. Aquí te doy datos útiles de la vida diaria, recetas, consejos, estudio, etc. (Luego conectamos IA real)"
    }

@app.post("/read_file")
async def read_file(file: UploadFile = File(...)):
    # Guarda el archivo
    with open(f"uploads/{file.filename}", "wb") as f:
        f.write(await file.read())
    return {
        "archivo": file.filename, 
        "mensaje": "✅ Archivo recibido. Puedo leer imágenes, videos y PDFs para analizarlos."
    }

@app.get("/health")
async def health():
    return {"status": "KIX funcionando al 100%", "proyecto": "AI-Omni"}
