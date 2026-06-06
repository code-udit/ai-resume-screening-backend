# AI Resume Screening Backend

### 👨‍💻 Developed By

**Udit U Gunagi**

An intelligent resume screening API built with FastAPI, scikit-learn, and spaCy that ranks candidate resumes against a job description using NLP, skill matching, experience analysis, and similarity scoring.

---

## 🔗 Links

### 🌐 Live Demo

https://ai-resume-screening-frontend-flame.vercel.app/

### 💻 Frontend Repository

https://github.com/code-udit/ai-resume-screening-frontend.git

### ⚙️ Backend Repository

https://github.com/code-udit/ai-resume-screening-backend.git

---

# 🚀 Overview

AI Resume Screening Backend helps recruiters and hiring teams automatically evaluate resumes by:

* Parsing uploaded resumes
* Extracting text from PDF and TXT files
* Comparing resumes against job descriptions
* Calculating skill match scores
* Evaluating experience requirements
* Generating ranked candidate results

The system uses a hybrid scoring approach combining NLP similarity, skill overlap, and experience matching.

---

# 🛠 Tech Stack

* FastAPI
* Python 3.11
* scikit-learn
* spaCy
* PyPDF2
* TF-IDF Vectorization
* Cosine Similarity
* Docker

---

# 🧱 System Architecture

```text
Recruiter
    │
    ▼
FastAPI API
    │
    ▼
Resume Parser
(PDF / TXT)
    │
    ▼
NLP Processing
(spaCy)
    │
    ▼
TF-IDF Vectorization
    │
    ▼
Cosine Similarity
    │
    ▼
Skill Matching
    │
    ▼
Experience Analysis
    │
    ▼
Final Ranking Engine
    │
    ▼
Ranked Candidates
```

---

# 📁 Project Structure

```bash
ai-resume-screening-backend/
│
├── app/
│   ├── main.py
│   ├── model.py
│   ├── scoring.py
│   ├── experience.py
│   ├── file_utils.py
│   ├── utils.py
│   └── logger.py
│
├── test_preprocess.py
├── test_ranking.py
│
├── requirements.txt
├── Dockerfile
├── runtime.txt
├── .render.yaml
└── README.md
```

---

# ✨ Features

## 📄 Resume Parsing

* PDF Resume Support
* TXT Resume Support
* Automatic Text Extraction
* Multi-Resume Upload

## 🧠 NLP Processing

* Text Cleaning
* Tokenization
* Lemmatization
* Stopword Removal
* Feature Extraction

## 🎯 Resume Matching

* TF-IDF Vectorization
* Cosine Similarity Scoring
* Job Description Comparison
* Candidate Ranking

## 🛠 Skill Matching

Built-in skill detection for:

* Python
* FastAPI
* Flask
* Django
* SQL
* SQLAlchemy
* Docker
* AWS
* Azure
* Machine Learning
* NLP
* TensorFlow
* PyTorch
* Git
* CI/CD

Skill matching uses spaCy PhraseMatcher to identify overlapping skills between job descriptions and resumes.

## 💼 Experience Analysis

The system extracts experience requirements such as:

```text
3 years
5+ years
2 years 6 months
```

Experience scores are calculated by comparing:

```text
Required Experience
        vs
Candidate Experience
```

## 📊 Hybrid Ranking Algorithm

Final score calculation:

```text
Final Score =
0.5 × Cosine Similarity
+ 0.3 × Skill Match Score
+ 0.2 × Experience Score
```

This provides a more accurate ranking than keyword matching alone.

---

# 🔄 Resume Ranking Workflow

1. Recruiter uploads resumes
2. Job description is submitted
3. Resume text is extracted
4. Text is preprocessed using spaCy
5. TF-IDF vectors are generated
6. Cosine similarity is calculated
7. Skill overlap is evaluated
8. Experience requirements are checked
9. Final hybrid score is calculated
10. Candidates are ranked from highest to lowest

---

# ⚙️ Environment Setup

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

Install spaCy model:

```bash
python -m spacy download en_core_web_sm
```

---

# ▶️ Run Application

```bash
uvicorn app.main:app --reload
```

Server starts at:

```bash
http://localhost:8000
```

---

# 📡 API Endpoints

## Health Check

### GET

```http
/health
```

Response:

```json
{
  "status": "ok"
}
```

---

## Rank Resumes

### POST

```http
/rank-files
```

### Form Data

| Field           | Type           |
| --------------- | -------------- |
| job_description | String         |
| resumes         | Multiple Files |

Supported file types:

* PDF
* TXT

---

### Sample Response

```json
[
  {
    "filename": "resume1.pdf",
    "final_score": 0.89,
    "cosine_score": 0.81,
    "skill_score": 1.0,
    "experience_score": 0.9
  },
  {
    "filename": "resume2.pdf",
    "final_score": 0.72,
    "cosine_score": 0.65,
    "skill_score": 0.8,
    "experience_score": 0.7
  }
]
```

---

# 📊 Scoring Components

| Component         | Weight |
| ----------------- | ------ |
| Cosine Similarity | 50%    |
| Skill Match       | 30%    |
| Experience Match  | 20%    |

---

# 🧪 Testing

Project includes:

```bash
test_preprocess.py
test_ranking.py
```

Run tests:

```bash
python test_preprocess.py

python test_ranking.py
```

---

# 🐳 Docker Support

Build Image:

```bash
docker build -t ai-resume-screening .
```

Run Container:

```bash
docker run -p 8000:8000 ai-resume-screening
```

---

# 📈 Future Improvements

* Resume Database Storage
* Candidate Dashboard
* JWT Authentication
* Advanced Skill Extraction
* Semantic Embeddings
* LLM-Based Resume Evaluation
* Recruiter Analytics
* Resume Recommendation Engine
* Batch Processing Queue
* Cloud Deployment

---

## 👨‍💻 Author

Developed by **Udit U Gunagi**


