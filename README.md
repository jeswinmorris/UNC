# Luna Prime - Free Online Server

## Deploy FREE 24/7 in 5 mins (No PC needed):

### Option A: HuggingFace Spaces (100% Free, Recommended)

1. Go to https://huggingface.co/new-space
   - Name: luna-prime-server
   - SDK: Docker
   - Hardware: CPU basic (FREE)
   - Visibility: Private (only you + friend)

2. Upload these 4 files from this ZIP:
   Dockerfile, server.py, start.sh, Modelfile-luna-prime

3. Wait 5-10 mins build. First boot pulls 2.5GB (3 mins).

4. Your URL will be:
   https://YOURNAME-luna-prime-server.hf.space

5. Test:
   https://YOURNAME-luna-prime-server.hf.space/
   Should show {"status": "Luna Prime Online"}

6. Friend on Mac 11 uses Luna UI and pastes that URL as Server.

### Option B: Railway.app (Faster, Free $5 credit)

1. Go to railway.app -> New Project -> Deploy from Dockerfile
2. Upload same files
3. It gives you public URL instantly, faster than HF.

### Option C: Render.com

1. render.com -> New Web Service -> Docker
2. Connect GitHub repo with these files
3. Free tier spins down after 15min, wakes on request.

All options work for Mac OS 11 friend - he just needs browser, no Ollama install.

Your friend uses the Luna Online Host Edition HTML I gave you, paste the public URL.
