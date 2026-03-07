An AI-powered cybersecurity tool that generates incident response and digital forensic investigation steps for different cyber attack scenarios. The system uses Flask for the backend and Google Gemini to generate structured security responses.

The tool helps security learners understand how to respond to cyber incidents and which forensic tools should be used during investigation.

Features
Secure Login Authentication
AI-based Incident Response Plan Generator
Generates step-by-step cyber forensic investigation steps
Export reports as TXT
Export reports as PDF
Simple web dashboard interface
Automated AI-generated cybersecurity guidance

Technologies Used
Python
Flask
Google Gemini API
HTML
CSS
FPDF (for PDF report generation)

Project Structure
incident-response-tool
│
├── app.py
├── requirements.txt
├── templates
│   ├── login.html
│   └── dashboard.html
│
├── static
│   └── style.css
│
└── README.md
Installation (Local Setup)

Clone the repository

git clone https://github.com/your-username/incident-response-tool.git

Move into the project folder

cd incident-response-tool

Install dependencies

pip install -r requirements.txt

Run the Flask application

python app.py

Open in browser

http://127.0.0.1:5000
Default Login Credentials
Username: admin
Password: 1234
Deployment (Render)

This project can be deployed easily using Render.

Step 1: Create requirements.txt
Flask
google-generativeai
fpdf
gunicorn
Step 2: Modify app run configuration
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
Step 3: Deploy on Render

Login to Render

Click New Web Service

Connect your GitHub repository

Configure settings:

Build Command

pip install -r requirements.txt

Start Command

gunicorn app:app
Step 4: Add Environment Variable

Add your Gemini API key in Render:

GEMINI_API_KEY = your_api_key

After deployment, Render will generate a public live link for the application.

Example Cyber Incident Scenarios

Users can test the system with scenarios like:

Ransomware attack on an organization network

Phishing email compromise

Suspicious login attempt on a server

Malware infection on employee workstation

Data breach investigation

The AI will generate incident response steps and recommended forensic tools.

Educational Purpose

This project is designed for cybersecurity learning and demonstration purposes, helping students understand:

Incident Response Workflow

Digital Forensics Investigation

Security Tool Usage

AI in Cybersecurity

Author

Riddhi Upadhyaya
Computer Science Student

Designed and Developed as a Cybersecurity Academic Project.
