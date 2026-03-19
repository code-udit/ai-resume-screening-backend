from app.utils import preprocess_text

sample = "I have 3 years of experience in Python, Machine Learning and NLP."

cleaned = preprocess_text(sample)

print(cleaned)