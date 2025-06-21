from fastapi import APIRouter, UploadFile, File
import tempfile
from typing import List
from .services import SimilarityMatch
from .schema import DataInput, Output
from .helper import get_random_string, create_resume_dir, create_job_description_dir
import os


ai_router = APIRouter()

@ai_router.post("/compare", response_model=Output)
async def generate_similarity(
    job_description: UploadFile = File(...),
    resume: UploadFile = File(...)
):
    # Define custom directories
    jd_dir = create_job_description_dir()
    resume_dir = create_resume_dir()

    # Save job description
    jd_path = os.path.join(jd_dir, f"{get_random_string()}.txt")
    with open(jd_path, "wb") as f:
        f.write(await job_description.read())

    # Save resume
    resume_path = os.path.join(resume_dir, f"{get_random_string()}.pdf")
    with open(resume_path, "wb") as f:
        f.write(await resume.read())

    print("***********")
    print(jd_path)
    print("***********")
    print(resume_path)
    print("***********")
    ai_service = SimilarityMatch(jd_path, resume_path)

    return ai_service.invoke()    
