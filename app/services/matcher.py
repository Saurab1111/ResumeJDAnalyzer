from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from app.services.text_preprocess import clean_text

def analyze_match(resume_text: str, jd_text: str):
    resume_clean = clean_text(resume_text)
    jd_clean = clean_text(jd_text)

    documents = [resume_clean, jd_clean]

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    match_score = round(similarity * 100, 2)

    feature_names = vectorizer.get_feature_names_out()

    resume_tokens = set(resume_clean.split())
    jd_tokens = set(jd_clean.split())

    matched_keywords = list(resume_tokens.intersection(jd_tokens))
    missing_keywords = list(jd_tokens - resume_tokens)

    return {
        "match_score": match_score,
        "matched_keywords": matched_keywords[:15],
        "missing_keywords": missing_keywords[:15],
    }
