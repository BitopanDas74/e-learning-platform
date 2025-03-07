from fastapi import FastAPI

app = FastAPI()  # Make sure this line exists

@app.get("/")
def home():
    return {"message": "Welcome to the AI-powered E-learning Platform"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


