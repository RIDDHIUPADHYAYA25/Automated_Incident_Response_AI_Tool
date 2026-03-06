Overview

The AI Incident Response & Forensics Assistant is a web-based cybersecurity tool that helps generate structured incident response plans for different cyber attack scenarios.
It uses Google Gemini AI to automatically produce step-by-step forensic and response procedures.
The system is built using Flask (Python) and provides a simple dashboard where users can input a cybersecurity scenario and receive a concise response plan.

Features
User authentication (Login system)
AI-generated incident response plans
Uses Google Gemini API
Short and structured AI responses
Export response as TXT file
Export response as PDF report
Simple and clean web interface

Technologies Used
Python
Flask
Google Gemini API
FPDF (PDF generation)
HTML / CSS
Session Management

Project Structure
project-folder
│
├── app.py
├── requirements.txt
│
├── templates
│   ├── login.html
│   └── dashboard.html
│
└── static
    └── style.css
    
Installation
1. Clone the repository
git clone https://github.com/yourusername/incident-response-ai.git
cd incident-response-ai
2. Install dependencies
pip install -r requirements.txt
3. Add your Gemini API Key
Replace the API key inside app.py
genai.configure(api_key="YOUR_API_KEY")
4. Run the application
python app.py
5. Open in browser
http://127.0.0.1:5000
Default Login Credentials
Username: admin
Password: 1234

How It Works
User logs into the system.
Enters a cybersecurity incident scenario.
The system sends the prompt to Gemini AI.
AI generates a step-by-step incident response plan.
The response can be downloaded as TXT or PDF.

Example Scenario
Phishing attack detected in company email server

Output will include:
Incident identification
Containment steps
Forensic evidence collection
Threat eradication
System recovery
Lessons learned
Applications
Cybersecurity learning
Incident response training
Forensic investigation planning
Academic cybersecurity projects

Future Improvements
Multiple user accounts
Incident report database
Log analysis integration
Automated evidence collection tools
Dashboard analytics

Author
Riddhi Upadhyaya
Computer Science Student | Cybersecurity Enthusiast | IoT Enthusiast | AI and ML Enthusiast
