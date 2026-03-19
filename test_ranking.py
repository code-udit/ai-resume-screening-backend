from app.model import ResumeRanker

job_description = """
Looking for a Python developer with experience in machine learning,
NLP, and data analysis.
"""

resumes = [
    "I have 3 years of experience in Python and machine learning.",
    "Frontend developer skilled in React and CSS.",
    "Data scientist with NLP and deep learning experience using Python."
]

ranker = ResumeRanker()
results = ranker.rank_resumes(job_description, resumes)

for resume, score in results:
    print(f"Score: {score:.4f}")
    print(f"Resume: {resume}")
    print("-" * 40)