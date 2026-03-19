# app/main.py

from app.logger import logger
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from app.model import ResumeRanker
from app.file_utils import extract_text_from_pdf
import io

app = FastAPI(title="AI Resume Screening API")

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ranker = ResumeRanker()


@app.post("/rank-files")
async def rank_resumes(
    job_description: str = Form(...),
    resumes: list[UploadFile] = File(...)
):

    logger.info("Received ranking request")
    logger.info(f"Job Description: {job_description[:100]}")

    resume_texts = []
    filenames = []

    try:
        for file in resumes:
            logger.info(f"Processing file: {file.filename}")

            content = await file.read()

            if file.filename.endswith(".pdf"):
                text = extract_text_from_pdf(io.BytesIO(content))
            elif file.filename.endswith(".txt"):
                text = content.decode("utf-8")
            else:
                logger.warning(f"Unsupported file type: {file.filename}")
                raise HTTPException(
                    status_code=400,
                    detail=f"Unsupported file type: {file.filename}"
                )

            resume_texts.append(text)
            filenames.append(file.filename)

        results = ranker.rank_resumes(job_description, resume_texts)

        logger.info("Ranking completed successfully")

        response = []

        for i, result in enumerate(results):
            logger.info(
                f"File: {filenames[i]} | "
                f"Final: {result['final_score']:.3f} | "
                f"Skill: {result['skill_score']:.3f} | "
                f"Exp: {result['experience_score']:.3f}"
            )

            response.append({
                "filename": filenames[i],
                "final_score": float(result["final_score"]),
                "cosine_score": float(result["cosine_score"]),
                "skill_score": float(result["skill_score"]),
                "experience_score": float(result["experience_score"])
            })

        return response

    except Exception as e:
        logger.error(f"Error during ranking: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))