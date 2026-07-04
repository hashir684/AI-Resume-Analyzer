
from text_processor import preprocess_text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_score(resume_text: str, job_text: str) -> float:
    """
    Compute similarity score between resume and job description
    using TF-IDF and cosine similarity.

    Args:
        resume_text (str): Raw resume text
        job_text (str): Raw job description text

    Returns:
        float: Match percentage    """

    processed_resume = preprocess_text(resume_text)
    processed_job = preprocess_text(job_text)

    if not processed_resume or not processed_job:
        return 0.0 
    
    vectorizer =TfidfVectorizer()
    
    tf_idf_matrix = vectorizer.fit_transform([processed_resume,processed_job])
    
    similarity = cosine_similarity(tf_idf_matrix)[0][1]
    match_percentage = round(similarity * 100, 2)

    return match_percentage

if __name__ == "__main__":
    resume = """
    Experienced Python Developer with expertise in
    Machine Learning, NLP, FastAPI, SQL, Docker and Git.
    """

    job_description = """
    We are looking for a Python Developer skilled in
    FastAPI, SQL, Docker, AWS and Git.
    """

    score = compute_score(resume, job_description)
    print(f"Resume–Job Match Score: {score}%")


