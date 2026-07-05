# AI Resume Analyzer
 
An AI-powered Resume Analyzer that compares a candidate's resume with a job description and provides:
 
- Resume text extraction (PDF/DOCX)
- Matching score based on TF-IDF similarity
- Skill gap analysis
- AI-generated feedback using LLM (TinyLlama via Ollama)
---
 
## Features
 
- Upload resume (PDF / DOCX)
- Paste job description
- TF-IDF-based similarity scoring
- Skill extraction & matching
- Weighted final score
- AI-powered feedback using TinyLlama
- FastAPI backend with auto-generated API docs
- Streamlit frontend for visualization
- Dockerized for easy setup
---
 
## Tech Stack
 
- **Backend:** FastAPI, Python
- **ML/NLP:** Scikit-learn, LangChain, NLTK, pdfplumber, python-docx
- **LLM:** Ollama (TinyLlama)
- **Frontend:** Streamlit
- **Containerization:** Docker, Docker Compose
---
 
## Project Structure
 
```
AI-Resume-Analyzer/
├── api/
│   ├── main_api.py
│   └── llm_help.py
├── models/
│   ├── final_score.py
│   ├── similarity_score.py
│   ├── skill.py
│   └── skill_match.py
├── utils/
│   ├── resume.py
│   └── text_processor.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── streamlit_app.py
```
 
---
 
## Quick Start (Docker)
 
### Prerequisites
- Docker & Docker Compose installed
### Run with Docker Compose
 
```bash
git clone https://github.com/hashir684/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
 
docker-compose up --build
```
 
This will:
1. Start FastAPI backend on `http://localhost:8000`
2. Start Ollama with TinyLlama
3. Start Streamlit frontend on `http://localhost:8501`
---
 
## API Documentation
 
Once running, visit:
 
```
http://localhost:8000/docs
```
 
Interactive Swagger UI with all endpoints and schemas.
 
---
 
## Manual Setup (Without Docker)
 
```bash
git clone https://github.com/hashir684/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
 
# Create virtual environment
python -m venv venv
venv\Scripts\activate   Windows
 
# Install dependencies
pip install -r requirements.txt
 
# Pull TinyLlama
ollama pull tinyllama
ollama run tinyllama  

uvicorn api.main_api:app --reload
 
# In another terminal, run Streamlit
streamlit run streamlit_app.py
```
 
---
 
## Usage
 
1. Open Streamlit UI
2. Upload your resume (PDF or DOCX)
3. Paste the job description
4. Click "Analyze"
5. Get matching score, skill gaps, and AI feedback
---
 
## 👨‍💻 Author
 
Muhammad Hashir Khan
 
---
 
## 📜 License
 
Educational Use Only
 
