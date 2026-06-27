from flask import Flask, render_template, request, redirect, url_for, session
import os

from resume_parser import extract_text
from skill_extractor import extract_skills
from ats_score import calculate_ats_score
from suggestions import generate_suggestions
from interview_questions import generate_questions

from database import create_database, save_resume, get_all_resumes
from user_database import (
    create_user_database,
    add_user,
    validate_user
)

app = Flask(__name__)

app.secret_key = "resume_analyzer_secret_key"

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create databases automatically
create_database()
create_user_database()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        username = request.form["username"]

        email = request.form["email"]

        password = request.form["password"]

        try:

            add_user(username, email, password)

            return redirect(url_for("login"))

        except:

            return "User already exists!"

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]

        password = request.form["password"]

        user = validate_user(email, password)

        if user:

            session["user"] = user[1]

            return redirect(url_for("home"))

        else:

            return "Invalid Email or Password"

    return render_template("login.html")


@app.route("/logout")
def logout():

    session.pop("user", None)

    return redirect(url_for("home"))


@app.route("/upload", methods=["GET", "POST"])
def upload():

    if "user" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        resume = request.files["resume"]

        if resume.filename != "":

            filepath = os.path.join(
                app.config["UPLOAD_FOLDER"],
                resume.filename
            )

            resume.save(filepath)

            text = extract_text(filepath)

            skills = extract_skills(text)

            ats_score = calculate_ats_score(text, skills)

            suggestions = generate_suggestions(text, skills)

            interview_questions = generate_questions(skills)

            save_resume(resume.filename, ats_score)

            return render_template(
                "result.html",
                resume_text=text,
                skills=skills,
                ats_score=ats_score,
                suggestions=suggestions,
                interview_questions=interview_questions
            )

    return render_template("upload.html")


@app.route("/history")
def history():

    if "user" not in session:
        return redirect(url_for("login"))

    resumes = get_all_resumes()

    return render_template(
        "history.html",
        resumes=resumes
    )


if __name__ == "__main__":
    app.run(debug=True)

