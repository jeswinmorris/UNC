from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import subprocess, time, os, json
import ollama

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

print("Starting ollama serve...")
subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(4)

def init_models():
    try:
        print("Pulling base model if needed...")
        # Pull directly via ollama binary for reliability
        subprocess.run(["ollama", "pull", "huihui_ai/qwen3-abliterated:4b-instruct-2507-q4_K_M"], check=False)
        if os.path.exists("/app/Modelfile-luna-prime"):
            print("Creating luna-prime:latest")
            subprocess.run(["ollama", "create", "luna-prime:latest", "-f", "/app/Modelfile-luna-prime"], check=False)
        print("Models ready!")
    except Exception as e:
        print(f"Init error: {e}")

init_models()

@app.get("/")
def root():
    return {"status": "Luna Prime Online sir!", "model": "luna-prime:latest", "api": "/api/chat"}

@app.get("/api/tags")
def tags():
    try:
        return ollama.list()
    except:
        return {"models": []}

@app.post("/api/chat")
async def chat(req: dict):
    model = req.get("model", "luna-prime:latest")
    messages = req.get("messages", [])
    stream = req.get("stream", False)
    from fastapi.responses import StreamingResponse
    def gen():
        try:
            response = ollama.chat(model=model, messages=messages, stream=True)
            for chunk in response:
                yield json.dumps(chunk) + "\n"
        except Exception as e:
            yield json.dumps({"error": str(e)}) + "\n"
    if stream:
        return StreamingResponse(gen(), media_type="application/x-ndjson")
    else:
        try:
            return ollama.chat(model=model, messages=messages)
        except Exception as e:
            # Fallback to binary
            return {"message": {"content": f"Error: {e}"}}
