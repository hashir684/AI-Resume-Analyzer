from langchain_community.llms import Ollama

llm = Ollama(
    model="tinyllama",
    num_predict=400,      
    temperature=0.5       
)


def generate_ai_feedback(analysis: dict) -> str:
    """
    Generate AI-based resume feedback using TinyLlama.

    Args:
        analysis (dict): Output from compute_final_score()

    Returns:
        str: AI-generated feedback text
    """

    matched_skills = ", ".join(analysis["matched_skills"]) if analysis["matched_skills"] else "None"
    missing_skills = ", ".join(analysis["missing_skills"]) if analysis["missing_skills"] else "None"

    prompt = f"""You are a recruiter. Review this resume:

Score: {analysis['final_score']}%
Has: {matched_skills}
Missing: {missing_skills}

Write professional feedback:

STRENGTHS:
[2-3 sentences about their skills]

AREAS TO IMPROVE:
[2-3 sentences about gaps]

RECOMMENDATIONS:
1. [First action]
2. [Second action]
3. [Third action]"""

    try:
        response = llm.invoke(prompt)
        
        cleanup_keywords = ["You are a recruiter", "Score:", "Has:", "Missing:", "Write professional feedback"]
        for keyword in cleanup_keywords:
            if keyword in response:
                parts = response.split(keyword)
                response = parts[-1].strip()
        
        if len(response) < 30:
            return "Unable to generate detailed feedback. Please try again."
        
        return response.strip()
        
    except Exception as e:
        return f"Error generating AI feedback: {str(e)}"