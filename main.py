from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Simple Backend API")

@app.get("/")
def read_root():
    return {"message": "Hello from collify backend!"}

@app.get("/api/health")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
