#!/bin/bash
set -e
echo "Starting ollama serve..."
ollama serve &
sleep 5
echo "Pulling model..."
ollama pull huihui_ai/qwen3-abliterated:4b-instruct-2507-q4_K_M || true
echo "Creating Luna..."
ollama create luna-prime:latest -f /app/Modelfile-luna-prime || true
echo "Luna ready sir!"
python3 -m uvicorn server:app --host 0.0.0.0 --port 10000
