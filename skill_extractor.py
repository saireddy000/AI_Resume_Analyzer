def extract_skills(text):

    skills = [
        "Python",
        "C",
        "C++",
        "Java",
        "SQL",
        "HTML",
        "CSS",
        "JavaScript",
        "MongoDB",
        "MySQL",
        "Git",
        "GitHub",
        "NumPy",
        "Pandas",
        "Matplotlib",
        "Flask",
        "Django",
        "Machine Learning",
        "Deep Learning",
        "Data Structures",
        "DBMS",
        "OOP"
    ]

    found_skills = []

    lower_text = text.lower()

    for skill in skills:

        if skill.lower() in lower_text:
            found_skills.append(skill)

    return found_skills