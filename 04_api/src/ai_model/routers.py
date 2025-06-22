from fastapi import APIRouter, UploadFile, File, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST
from .services import SimilarityMatch
from .schema import Output
from .helper import create_resume_dir, create_job_description_dir, upload_file


ai_router = APIRouter()

@ai_router.post("/compare", response_model=Output)
async def generate_similarity(
    job_description: UploadFile = File(...),
    resume: UploadFile = File(...)
):
    if not job_description.filename.lower().endswith(".txt"):
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="Job description must be a Text file (.txt)."
        )

    if not resume.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="Resume must be a PDF file (.pdf)."
        )

    jd_dir = create_job_description_dir()
    resume_dir = create_resume_dir()

    jd_path = await upload_file(job_description, jd_dir)
    resume_path = await upload_file(resume, resume_dir)

    ai_service = SimilarityMatch(jd_path, resume_path)

    return ai_service.invoke()
