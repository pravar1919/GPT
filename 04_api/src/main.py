from fastapi import FastAPI
from src.ai_model.routers import ai_router

version = "v1"
app = FastAPI(
    title="Job Match API",
    description="API to compare job descriptions and resumes using AI",
    version=version
)


@app.get("/")
def home():
    return "success"

app.include_router(ai_router, prefix=f"/api/{version}", tags=["Compare"])

if __name__ == "__main__":
    app.run(host="localhost", port="8000")


