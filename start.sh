#!/bin/bash
ollama serve &
sleep 3
(
  echo "Pulling base model 2.5GB..."
  ollama pull huihui_ai/qwen3-abliterated:4b-instruct-2507-q4_K_M
  echo "Creating luna-prime..."
  ollama create luna-prime:latest -f /app/Modelfile-luna-prime
  echo "Ready sir!"
) &
python3 -m uvicorn server:app --host 0.0.0.0 --port 7860
