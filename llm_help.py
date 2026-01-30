from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate

llm = Ollama(model="tinyllama")


def generate_ai_feedback(analysis: dict) -> str:
    """
    Generate AI-based resume feedback using TinyLlama.

    Args:
        analysis (dict): Output from compute_final_score()

    Returns:
        str: AI-generated feedback text
    """

    prompt_template = PromptTemplate(
        input_variables=[
            "final_score",
            "skill_score",
            "tfidf_score",
            "matched_skills",
            "missing_skills"
        ],
        template="""
You are an experienced technical recruiter and resume reviewer.

Resume analysis results:
- Final Score: {final_score}%
- Skill Match Score: {skill_score}%
- Text Similarity Score: {tfidf_score}%

Matched Skills:
{matched_skills}

Missing Skills:
{missing_skills}

Tasks:
1. Briefly explain the strengths of the resume
2. Identify weak areas
3. Suggest 2–3 concrete improvements

Rules:
- Do NOT invent skills
- Base your response ONLY on the provided data
- Keep the tone professional and concise
"""
    )

    prompt = prompt_template.format(
        final_score=analysis["final_score"],
        skill_score=analysis["skill_match_score"],
        tfidf_score=analysis["tfidf_score"],
        matched_skills=", ".join(analysis["matched_skills"]) or "None",
        missing_skills=", ".join(analysis["missing_skills"]) or "None"
    )

    response = llm.invoke(prompt)  
    return response.strip()