from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.ai_model.routers import ai_router
from src.auth.routers import auth_router


version = "v1"
app = FastAPI(
    title="Job Match API",
    description="API to compare job descriptions and resumes using AI",
    version=version
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://939b-2409-40d4-16f-62f5-38f9-9e4d-a638-48c3.ngrok-free.app"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return "success"

app.include_router(ai_router, prefix=f"/api/{version}", tags=["Compare"])
app.include_router(auth_router, prefix=f"/api/{version}/auth", tags=["Auth"])

if __name__ == "__main__":
    app.run(host="localhost", port="8000")


