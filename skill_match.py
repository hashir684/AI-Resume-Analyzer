from text_processor import preprocess_text
from skill import skills


def extract_skills(text: str) -> set:
    """
    Extract skills from text using rule-based matching.

    Args:
        text (str): Raw resume or job description text.

    Returns:
        set: Unique skills found in the text.
    """

    if not text or not text.strip():
        return set()

    processed_text = preprocess_text(text)
    found_skills = set()

    for s in skills:
        if s.lower() in processed_text:
            found_skills.add(s.lower())

    return found_skills


def compute_match(resume_text: str, job_text: str) -> dict:
    """
    Compute skill match score between resume and job description.

    Args:
        resume_text (str): Resume text
        job_text (str): Job description text

    Returns:
        dict: Skill match details
    """

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_text)

    if not job_skills:
        return {
            "score": 0.0,
            "matched_skills": [],
            "missing_skills": []
        }

    matched = resume_skills.intersection(job_skills)
    missing = job_skills - resume_skills

    score = (len(matched) / len(job_skills)) * 100

    return {
        "score": round(score, 2),
        "matched_skills": sorted(matched),
        "missing_skills": sorted(missing)
    }


if __name__ == "__main__":
    resume = """
    Experienced Python Developer with expertise in
    Machine Learning, NLP, FastAPI, SQL, Docker and Git.
    """

    job = """
    Looking for a Python Developer skilled in
    FastAPI, SQL, Docker, AWS and Git.
    """

    result = compute_match(resume, job)
    print("Skill Match Result:", result)
