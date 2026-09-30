FROM ollama/ollama:latest

# Fix pip issue on ollama base
RUN apt-get update && apt-get install -y python3 python3-pip curl && rm -rf /var/lib/apt/lists/*
RUN pip3 install --break-system-packages --no-cache-dir fastapi uvicorn ollama pydantic h11

WORKDIR /app

COPY server.py /app/server.py
COPY Modelfile-luna-prime /app/Modelfile-luna-prime
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

EXPOSE 7860
EXPOSE 11434

CMD ["/app/start.sh"]
