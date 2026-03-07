from flask import Flask, render_template, request, redirect, url_for, Response, session, flash
import google.generativeai as genai
from fpdf import FPDF
import logging
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "fallback_secret")

# Logging for debugging
logging.basicConfig(level=logging.INFO)

# Configure Gemini API
try:
    genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-2.5-flash")
except Exception as e:
    logging.error("Gemini configuration failed: %s", e)
    model = None

# Hardcoded credentials
USERNAME = "admin"
PASSWORD = "1234"


# ---------------- AI RESPONSE FUNCTION ---------------- #

def get_ai_response(scenario):

    prompt = f"""
You are a cybersecurity incident response expert.

Provide a SHORT and CLEAR incident response plan.

Structure:
1. Incident Identification
2. Containment Steps
3. Evidence Collection
4. Forensic Tools
5. Recovery Steps

Use bullet points and keep the answer concise.

Scenario: {scenario}
"""

    try:
        if model:
            response = model.generate_content(
                prompt,
                generation_config={
                    "max_output_tokens": 200,   # Limits length
                    "temperature": 0.3          # Keeps answers focused
                }
            )

            return response.text.strip()

        else:
            raise Exception("AI model unavailable")

    except Exception as e:
        logging.error("AI Error: %s", e)

        return (
            f"Sample Incident Response Plan for: {scenario}\n\n"
            "1. Incident Identification\n"
            "- Suspicious activity detected\n\n"
            "2. Containment\n"
            "- Isolate affected systems\n\n"
            "3. Evidence Collection\n"
            "- Collect logs and memory dump\n\n"
            "4. Forensic Tools\n"
            "- Wireshark\n"
            "- Autopsy\n"
            "- Volatility\n\n"
            "5. Recovery\n"
            "- Remove malware and restore backups"
        )


# ---------------- LOGIN ROUTE ---------------- #

@app.route("/", methods=["GET", "POST"])
def login():

    try:
        if request.method == "POST":

            username = request.form.get("username")
            password = request.form.get("password")

            if username == USERNAME and password == PASSWORD:
                session["logged_in"] = True
                return redirect(url_for("dashboard"))

            else:
                flash("Invalid credentials")

        return render_template("login.html")

    except Exception as e:
        logging.error("Login error: %s", e)
        return "Login system error", 500


# ---------------- DASHBOARD ROUTE ---------------- #

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():

    if "logged_in" not in session:
        return redirect(url_for("login"))

    response = ""

    try:

        if request.method == "POST":

            scenario = request.form.get("scenario")

            if scenario:
                response = get_ai_response(scenario)

        return render_template("dashboard.html", response=response)

    except Exception as e:
        logging.error("Dashboard error: %s", e)
        return "Dashboard error occurred", 500


# ---------------- LOGOUT ---------------- #

@app.route("/logout")
def logout():

    session.clear()
    return redirect(url_for("login"))


# ---------------- EXPORT TXT ---------------- #

@app.route("/export/txt", methods=["POST"])
def export_txt():

    if "logged_in" not in session:
        return redirect(url_for("login"))

    try:
        response_text = request.form.get("response")

        return Response(
            response_text,
            mimetype="text/plain",
            headers={
                "Content-Disposition": "attachment;filename=incident_report.txt"
            }
        )

    except Exception as e:
        logging.error("TXT export error: %s", e)
        return "TXT export failed", 500


# ---------------- EXPORT PDF ---------------- #

@app.route("/export/pdf", methods=["POST"])
def export_pdf():

    if "logged_in" not in session:
        return redirect(url_for("login"))

    try:
        response_text = request.form.get("response")

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.multi_cell(0, 10, response_text)

        pdf_output = pdf.output(dest="S").encode("latin-1")

        return Response(
            pdf_output,
            mimetype="application/pdf",
            headers={
                "Content-Disposition": "attachment;filename=incident_report.pdf"
            }
        )

    except Exception as e:
        logging.error("PDF export error: %s", e)
        return "PDF generation failed", 500


# ---------------- RUN APP ---------------- #

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)