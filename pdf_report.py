from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def create_pdf(filename, ats_score, skills, suggestions, interview_questions):

    c = canvas.Canvas(filename, pagesize=letter)

    y = 750

    c.setFont("Helvetica-Bold", 18)
    c.drawString(150, y, "AI Resume Analyzer Report")

    y -= 40

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, f"ATS Score : {ats_score}/100")

    y -= 40

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Skills")

    y -= 25

    c.setFont("Helvetica", 12)

    for skill in skills:
        c.drawString(70, y, "• " + skill)
        y -= 20

    y -= 15

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Suggestions")

    y -= 25

    c.setFont("Helvetica", 12)

    for suggestion in suggestions:
        c.drawString(70, y, "• " + suggestion)
        y -= 20

    y -= 15

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Interview Questions")

    y -= 25

    c.setFont("Helvetica", 12)

    for skill, questions in interview_questions.items():

        c.drawString(60, y, skill)

        y -= 20

        for question in questions:

            c.drawString(80, y, "- " + question)

            y -= 20

            if y < 60:
                c.showPage()
                y = 750
                c.setFont("Helvetica", 12)

        y -= 10

    c.save()