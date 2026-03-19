# app/experience.py

import re


def extract_years_experience(text: str) -> float:
    """
    Extract total years of experience from text.
    Supports patterns like:
    - 3 years
    - 3+ years
    - 3 years 6 months
    """

    text = text.lower()

    year_match = re.search(r'(\d+)\+?\s*year', text)
    month_match = re.search(r'(\d+)\s*month', text)

    years = 0
    months = 0

    if year_match:
        years = int(year_match.group(1))

    if month_match:
        months = int(month_match.group(1))

    total_years = years + (months / 12)

    return total_years


def experience_score(jd_text: str, resume_text: str) -> float:
    """
    Compare required experience vs resume experience.
    Returns score between 0 and 1.
    """

    required_exp = extract_years_experience(jd_text)
    candidate_exp = extract_years_experience(resume_text)

    if required_exp == 0:
        return 0.5  # neutral score if JD doesn't specify experience

    if candidate_exp >= required_exp:
        return 1.0

    return candidate_exp / required_exp