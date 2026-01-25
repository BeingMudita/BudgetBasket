from fastapi import FastAPI

app = FastAPI(title="Quick Commerce Price Engine")

@app.get("/health")
def health():
    return {"status": "ok"}
