from fastapi import FastAPI

app = FastAPI(title="ASK-MY-NOTES API")

@app.get("/")
def home():
    return {"message": "ASK-MY-NOTES Backend is running"}

@app.get("/health")
def health():
    return {"status": "OK"}