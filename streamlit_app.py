import streamlit as st
import requests

API_URL = "http://127.0.0.1:8001/analyze-resume/"

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="centered"
)

st.markdown(
    """
    <style>
    /* Navy blue background */
    .stApp {
        background-color: #021526;
    }
    
    /* Make content area white */
    .main .block-container {
        background-color: white;
        padding: 2rem;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("AI Resume Analyzer")
st.write("Upload your resume and paste job description to get AI-powered analysis.")

resume_file = st.file_uploader(
    "Upload Resume (PDF/DOCX)",
    type=["pdf", "docx"]
)

job_desc = st.text_area(
    "Paste Job Description",
    height=200,
    placeholder="Enter the job requirements, skills, and qualifications..."
)

if st.button("Analyze Resume", type="primary"):
    if resume_file is None:
        st.warning("Please upload a resume.")
    
    elif not job_desc.strip():
        st.warning("Please enter job description.")
    
    else:
        with st.spinner("Analyzing your resume with AI... Please wait"):
            files = {
                "resume": resume_file
            }
            data = {
                "job_description": job_desc
            }
            
            try:
                response = requests.post(
                    API_URL,
                    files=files,
                    data=data,
                    timeout=120
                )
                
                if response.status_code == 200:
                    result_data = response.json()
                    result = result_data["analysis"]
                    ai_feedback = result_data.get("ai_feedback", "AI feedback not available")
                    
                    st.success("Analysis Complete!")
                    
                    tab1, tab2 = st.tabs(["Scores & Skills", "AI Feedback"])
                    
                    with tab1:
                        st.subheader("Match Scores")
                        
                        col1, col2, col3 = st.columns(3)    
                        with col1:
                            st.metric(
                                label="Final Score",
                                value=f"{result['final_score']}%"
                            )
                        
                        with col2:
                            st.metric(
                                label="Skill Match",
                                value=f"{result['skill_match_score']}%"
                            )
                        
                        with col3:
                            st.metric(
                                label="Text Similarity",
                                value=f"{result['tfidf_score']}%"
                            )
                        
                        st.divider()
                        
                        st.subheader("Matched Skills")
                        if result["matched_skills"]:
                            skills_html = " ".join([
                                f'<span style="background-color: #d4edda; color: #155724; padding: 5px 10px; border-radius: 5px; margin: 3px; display: inline-block;">{skill}</span>'
                                for skill in result["matched_skills"]
                            ])
                            st.markdown(skills_html, unsafe_allow_html=True)
                        else:
                            st.write("No matched skills found.")
                        
                        st.divider()
                        
                        st.subheader("Missing Skills")
                        if result["missing_skills"]:
                            skills_html = " ".join([
                                f'<span style="background-color: #f8d7da; color: #721c24; padding: 5px 10px; border-radius: 5px; margin: 3px; display: inline-block;">{skill}</span>'
                                for skill in result["missing_skills"]
                            ])
                            st.markdown(skills_html, unsafe_allow_html=True)
                        else:
                            st.write("No missing skills.")
                    
                    with tab2:
                        st.subheader("🤖 AI-Powered Feedback")
                        
                        st.markdown(
                            f"""
                            <div style="background-color: #f0f8ff; padding: 20px; border-radius: 10px; border-left: 5px solid #4CAF50;">
                                <div style="color: #333; line-height: 1.8; white-space: pre-wrap;">{ai_feedback}</div>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
                        
                        st.download_button(
                            label="📥 Download Feedback",
                            data=ai_feedback,
                            file_name="resume_feedback.txt",
                            mime="text/plain"
                        )
                
                else:
                    st.error(f"Server Error: {response.status_code}")
                    if response.text:
                        st.error(f"Details: {response.text}")
            
            except requests.exceptions.Timeout:
                st.error("Request timed out. The analysis is taking too long. Please try again.")
            
            except requests.exceptions.ConnectionError:
                st.error("Cannot connect to the backend API. Make sure the FastAPI server is running.")
                st.info("Run: `uvicorn main_api:app --reload`")
            
            except Exception as e:
                st.error(f"Error: {str(e)}")