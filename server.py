
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import subprocess, time, os, json
import ollama

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

print("Starting ollama serve...")
subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(3)

def init_models():
    try:
        print("Checking models...")
        ollama.pull("huihui_ai/qwen3-abliterated:4b-instruct-2507-q4_K_M")
        if os.path.exists("/app/Modelfile-luna-prime"):
            with open("/app/Modelfile-luna-prime") as f:
                mf = f.read()
            ollama.create(model="luna-prime:latest", modelfile=mf)
        print("Models ready!")
    except Exception as e:
        print(f"Init error: {e}")

init_models()

@app.get("/")
def root():
    return {"status": "Luna Prime Online", "model": "luna-prime:latest"}

@app.post("/api/chat")
async def chat(req: dict):
    model = req.get("model", "luna-prime:latest")
    messages = req.get("messages", [])
    stream = req.get("stream", False)
    def gen():
        response = ollama.chat(model=model, messages=messages, stream=True)
        for chunk in response:
            yield json.dumps(chunk) + "\n"
    if stream:
        return StreamingResponse(gen(), media_type="application/x-ndjson")
    else:
        return ollama.chat(model=model, messages=messages)

@app.get("/api/tags")
def tags():
    return ollama.list()
