The Loyalty Project
- Turn First-Timers into Forever Fans.

The Loyalty Project is a full-stack application designed to tackle one of the most critical product challenges — customer drop-off after the first use.

It combines:
🧠 Feedback Intelligence
🖼️ UI/UX Analysis
to convert raw inputs into actionable product improvements.

Problem Statement : Most products don’t fail because they lack features — they fail because users leave before discovering value. (Customer drop after first use)

Users drop off after their first interaction due to:
i.Confusing onboarding
ii.Poor UI/UX
iii.Performance issues
iv.Lack of perceived value

The real challenge is: Teams don’t know why users leave — they guess.

Solution

The Loyalty Project eliminates guesswork by:
1.Detecting problems from real feedback
2.Analyzing UI for friction points
3.Generating structured solutions

Core Features
-> Voice to Value
“Every feedback is a clue. We decode it.”
Description : Stop guessing why customers leave. Voice to Value transforms raw customer feedback into:
Clear problem statements
Categorized issues
Actionable solutions with templates

So you fix what actually hurts, not what you assume does.

-> First Impressions
“See your product the way your customers do — for the first time, every time.”
Description : A confusing interface is a silent exit door. First Impressions audits your website’s UI/UX using computer vision and delivers:
Visual complexity insights
Layout detection (mobile vs desktop)
Readability & contrast evaluation
Friction point identification
So your product feels intuitive from the very first click.

Tech Stack
Frontend:
HTML
Tailwind CSS
JavaScript

Backend:
FastAPI (Python)
Computer Vision
OpenCV
NumPy
JSON

Swagger UI used for checking the backend. 
Built on VS Code. 

Project Structure

the loyalty project/
│
├── Backend/
│   ├── main.py
│   ├── analyzer.py
│   ├── templates_data.json
│
├── Frontend/
│   ├── index.html
│   ├── feedback.html
│   ├── ui.html
│   ├── script.js
│   ├── ui.js
│
│
└── README.md

Backend Setup:
cd Backend
pip install fastapi uvicorn python-multipart opencv-python numpy

Run backend:
uvicorn main:app --reload

Frontend Setup:
cd Frontend
python -m http.server 5500

Open:
http://127.0.0.1:5500 (localhost)

API Endpoints
Feedback Analysis : POST /analyze
UI Analysis : POST /analyze-ui

How It Works

Feedback Analysis

Input feedback
Keyword detection
Issue categorization
Solution + template generation

UI Analysis

Upload UI screenshot
Image preprocessing
Edge detection (complexity)
Contour detection (elements)
Brightness & layout analysis
Insight generation

Future Improvements

AI-based NLP (instead of keyword matching)
Deep learning UI detection
Real-time product analytics
SaaS dashboard version

Author : Sajani Manimala 
www.linkedin.com/in/sajani-manimala
© 2026 Sajani M. All rights reserved.
