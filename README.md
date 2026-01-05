Smart Resume–Job Match Analyzer
📌 Overview

Smart Resume–Job Match Analyzer is an offline, ML-based application that evaluates how well a candidate’s resume matches a given job description. The system uses classical NLP and Machine Learning techniques to compute similarity scores, identify overlapping skills, and highlight missing keywords — similar to an ATS-style screening system.

The project runs fully locally and does not require any external API keys or LLM services.

🎯 Problem Statement

Manual resume screening is time-consuming and subjective. Recruiters and candidates often struggle to:

Assess resume–job fit objectively

Identify missing or weak skills

Optimize resumes for ATS systems

This project automates resume screening using deterministic, explainable ML logic.

🧠 Solution Approach (No API / No LLM)

Input

Resume text

Job Description text

Text Preprocessing

Lowercasing

Tokenization

Stop-word removal

Text normalization

Feature Engineering

Resume and JD converted into vectors using TF-IDF

Important skill-related terms are weighted automatically

Matching & Scoring

Similarity score calculated between resume and JD

Matching and missing keywords identified

Output

Resume–JD match percentage

Matched keywords

Missing keywords

🏗️ Architecture (Conceptual)
Resume Text ──┐
              ├─► Text Preprocessing ─► TF-IDF Vectorization ─► Similarity Scoring
Job Description ─┘

🧩 Tech Stack

Language: Python

Backend Framework: FastAPI

ML / NLP: TF-IDF (Scikit-learn)

Data Processing: NumPy, Pandas

API Docs: Swagger (FastAPI)

✔ Fully offline
✔ No OpenAI / no LLM / no paid APIs

🚀 How to Run Locally
Prerequisites

Python 3.9+

Git

1️⃣ Clone the Repository
git clone https://github.com/your-username/resume-jd-analyzer.git
cd resume-jd-analyzer

2️⃣ Create & Activate Virtual Environment

Windows

python -m venv venv
venv\Scripts\activate


macOS / Linux

python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Start the Server
uvicorn app.main:app --reload


Server runs at:

http://127.0.0.1:8000

5️⃣ Open API Documentation
http://127.0.0.1:8000/docs


Use Swagger UI to test the API.

📌 Sample API Request
{
  "resume_text": "Python developer with AWS and REST API experience",
  "jd_text": "Looking for Python backend engineer with AWS and REST APIs"
}

📌 Sample Response
{
  "match_score": 74.82,
  "matched_keywords": ["python", "aws", "rest"],
  "missing_keywords": ["backend", "engineer"]
}

🧪 What Was Tested

Text preprocessing pipeline

TF-IDF vectorization

Similarity scoring accuracy

End-to-end API execution

The system was validated locally without any external dependencies.

📈 Future Enhancements

Skill weighting

PDF resume upload

Multi-resume ranking

LLM-based resume feedback (optional)

Dockerized deployment