# app/scoring.py

import spacy
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_sm")

# Expandable skill list
SKILL_PATTERNS = [
    "python",
    "flask",
    "fastapi",
    "django",
    "rest api",
    "sql",
    "sqlalchemy",
    "mysql",
    "oracle",
    "docker",
    "aws",
    "azure",
    "azure devops",
    "machine learning",
    "ml",
    "nlp",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "git",
    "ci/cd"
]

matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
patterns = [nlp.make_doc(skill) for skill in SKILL_PATTERNS]
matcher.add("SKILLS", patterns)


def extract_skills(text: str):
    doc = nlp(text)
    matches = matcher(doc)

    found_skills = set()

    for match_id, start, end in matches:
        skill = doc[start:end].text.lower()
        found_skills.add(skill)

    return found_skills


def skill_overlap_score(job_description: str, resume: str):

    jd_skills = extract_skills(job_description)
    resume_skills = extract_skills(resume)

    if not jd_skills:
        return 0.0

    overlap = jd_skills.intersection(resume_skills)

    return len(overlap) / len(jd_skills)