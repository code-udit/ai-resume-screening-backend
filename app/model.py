# app/model.py

from app.experience import experience_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from app.utils import preprocess_text
from app.scoring import skill_overlap_score


class ResumeRanker:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def rank_resumes(self, job_description: str, resumes: list[str]):

        cleaned_jd = preprocess_text(job_description)
        cleaned_resumes = [preprocess_text(resume) for resume in resumes]
    
        documents = [cleaned_jd] + cleaned_resumes
        tfidf_matrix = self.vectorizer.fit_transform(documents)
    
        jd_vector = tfidf_matrix[0]
        resume_vectors = tfidf_matrix[1:]
    
        cosine_scores = cosine_similarity(jd_vector, resume_vectors)[0]
    
        ranked_results = []
    
        for i, resume in enumerate(resumes):
        
            skill_score = skill_overlap_score(job_description, resume)
    
            exp_score = experience_score(job_description, resume)
    
            # Final upgraded hybrid formula
            final_score = (
                0.5 * cosine_scores[i] +
                0.3 * skill_score +
                0.2 * exp_score
            )
    
            ranked_results.append({
                "resume": resume,
                "final_score": final_score,
                "cosine_score": cosine_scores[i],
                "skill_score": skill_score,
                "experience_score": exp_score
            })
    
        ranked_results.sort(key=lambda x: x["final_score"], reverse=True)
    
        return ranked_results