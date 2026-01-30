from fastapi import FastAPI, UploadFile, File, Form, HTTPException
import shutil
import os
from resume import extract_resume_text
from final_score import compute_final_score
from llm_help import generate_ai_feedback  

app = FastAPI(title="Resume Analyzer API")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/analyze-resume/")
async def analyze_resume(resume: UploadFile = File(...), job_description: str = Form(...) ):
    """
    Analyze resume against job description and provide AI feedback.
    """
    
    if not resume.filename.lower().endswith((".pdf", ".docx")):
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX resumes are supported"
        )

    file_path = os.path.join(UPLOAD_DIR, resume.filename)

    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(resume.file, buffer)

        resume_text = extract_resume_text(file_path)
        result = compute_final_score(resume_text, job_description)
        ai_feedback = generate_ai_feedback(result)

        return {
            "filename": resume.filename,
            "analysis": result,
            "AI_feedback": ai_feedback  
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        resume.file.close()
        if os.path.exists(file_path):
            os.remove(file_path)