# EduGen AI

## AI-Powered Educational Content Generation Platform

EduGen AI is an Agentic AI-based educational content generation system that helps teachers automatically create:

*  Lesson Plans
*  Teacher Notes
*  Quizzes
*  Classroom Activities
*  Learning Outcomes

using Generative AI.

---

#  Features

## AI Features

* Prompt Engineering
* Agentic AI Architecture
* AEO (Answer Engine Optimization)
* GEO (Generative Engine Optimization)
* AI Tool Stacking
* LLM Management
* Gemini Integration

---

## Educational Content Generation

Generate:

* Lesson Plans
* Teacher Notes
* Quizzes
* Activities
* Learning Outcomes

for any:

* Subject
* Grade
* Topic
* Duration

---

## Export Features

Supported formats:

* TXT Export
* DOCX Export
* PDF Export

---

## Database Features

* SQLite Database
* History Tracking
* Recent Activity
* Dashboard Statistics
* Clear History

---

#  Project Architecture

User

↓

Streamlit Frontend

↓

Main Agent

↓

Specialized Agents

↓

Prompt Layer

↓

Gemini Service

↓

Database

↓

Export Layer

---

#  Technologies Used

## Frontend

* Streamlit

## Backend

* Python

## Database

* SQLite

## AI Model

* Gemini API

## Libraries

* google-genai
* python-dotenv
* python-docx
* reportlab

---

#  Project Structure

EduGenAI/

├── agents/

├── database/

├── llm/

├── prompts/

├── utils/

├── output/

├── docs/

├── app.py

├── requirements.txt

└── README.md

---

#  Installation

## Clone Repository

git clone YOUR_REPOSITORY_URL

cd EduGenAI

---

## Create Virtual Environment

python -m venv venv

---

## Activate Virtual Environment

Windows:

venv\Scripts\activate

---

## Install Dependencies

pip install -r requirements.txt

---

## Configure Environment Variables

Create:

.env

Add:

GEMINI_API_KEY=YOUR_API_KEY

---

#  Run Application

streamlit run app.py

Application URL:

http://localhost:8501

---

#  Application Modules

* Dashboard
* Generate Content
* History
* Settings

---

#  Export Options

* TXT
* DOCX
* PDF

---

#  Future Enhancements

* PowerPoint Generation
* Multi-Agent Collaboration
* User Authentication
* Curriculum Mapping
* Cloud Deployment
* AI Analytics Dashboard

---

#  Author

Project: EduGen AI

Technology Stack:

Python + Streamlit + Gemini AI + SQLite + DOCX + PDF

---

#  License

This project is developed for educational and research purposes.
