def generate_suggestions(text, skills):

    suggestions = []

    lower_text = text.lower()

    if len(skills) < 8:
        suggestions.append("Add more technical skills.")

    if "github" not in lower_text:
        suggestions.append("Add your GitHub profile.")

    if "linkedin" not in lower_text:
        suggestions.append("Add your LinkedIn profile.")

    if "project" not in lower_text:
        suggestions.append("Add at least 2 strong projects.")

    if "experience" not in lower_text:
        suggestions.append("Include internships or work experience.")

    if "certification" not in lower_text:
        suggestions.append("Add relevant certifications.")

    if "summary" not in lower_text:
        suggestions.append("Add a professional summary section.")

    if "achievement" not in lower_text:
        suggestions.append("Mention measurable achievements.")

    if len(suggestions) == 0:
        suggestions.append("Excellent Resume! Very few improvements needed.")

    return suggestions