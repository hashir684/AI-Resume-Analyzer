# AI Resume Analyzer

An AI-powered Resume Analyzer that compares a candidate's resume with a job description and provides:

- Resume text extraction (PDF/DOCX)
- Matching score
- Skill gap analysis
- AI-generated feedback (using TinyLlama)

---

## Features

- Upload resume (PDF / DOCX)  
- Paste job description  
- TF-IDF similarity scoring  
- Skill matching  
- Final weighted score  
- AI feedback using TinyLlama (Ollama)  
- FastAPI backend  
- Streamlit for visuals

---

## Tech Stack

- Python
- FastAPI
- Scikit-learn
- LangChain
- Ollama (TinyLlama)
- Streamlit
- pdfplumber
- python-docx
- NLTK
- VS Code

---

## Project Structure

```
Resume-analyzer/
- main_api.py
- resume.py
- text_processor.py
- skill.py
- skill_match.py
- similarity_score.py
- final_score.py
- llm_helper.py

---

## Installation

```bash
git clone https://github.com/hashir684/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## Setup TinyLlama

```bash
ollama pull tinyllama
ollama run tinyllama
```

---

## Run Server

```bash
uvicorn main_api:app --reload
```

Visit:

http://127.0.0.1:8000/docs

---

## 👨‍💻 Author

Muhammad Hashir Khan

---

## 📜 License

Educational Use Only
