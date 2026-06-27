def calculate_ats_score(text, skills):

    score = 0

    # Skills Score (Maximum 50)
    score += min(len(skills) * 5, 50)

    lower_text = text.lower()

    if "education" in lower_text:
        score += 10

    if "project" in lower_text:
        score += 10

    if "experience" in lower_text:
        score += 10

    if "certification" in lower_text:
        score += 10

    if "@" in text:
        score += 10

    return score