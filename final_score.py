import json
from similarity_score import compute_score
from skill_match import compute_match 

def compute_final_score(resume_text: str, job_text: str, skill_weight: float = 0.7, text_weight: float = 0.3) -> dict:
    """
    Compute final resume-job fit score by combining
    TF-IDF similarity and skill match score.

    Args:
        resume_text (str): Raw resume text
        job_text (str): Raw job description text
        skill_weight (float): Weight for skill match (default 0.7)
        text_weight (float): Weight for TF-IDF similarity (default 0.3)

    Returns:
        dict: Final score and skill match details
    """

    if not resume_text.strip() or not job_text.strip():
        return {
            "final_score": 0.0,
            "skill_match_score": 0.0,
            "tfidf_score": 0.0,
            "matched_skills": [],
            "missing_skills": []
        }

    text_score = float(compute_score(resume_text, job_text))
    skill_result = compute_match(resume_text, job_text)
    skill_score = float(skill_result["score"])

    final_score = float(round((skill_weight * skill_score) + (text_weight * text_score), 2))

    return {
        "final_score": final_score,
        "skill_match_score": skill_score,
        "tfidf_score": text_score,
        "matched_skills": skill_result["matched_skills"],
        "missing_skills": skill_result["missing_skills"]
    }


if __name__ == "__main__":
    resume = """
    Experienced Python Developer with expertise in
    Machine Learning, NLP, FastAPI, SQL, Docker and Git.
    """

    job = """
    We are looking for a Python Developer skilled in
    FastAPI, SQL, Docker, AWS and Git.
    """

    result = compute_final_score(resume, job)
    
    print("Final Resume-Job Description Matching Result:")
    print(json.dumps(result, indent=4))
