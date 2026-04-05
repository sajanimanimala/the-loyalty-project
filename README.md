 # 🚀 The Loyalty Project

### *Turn First-Timers into Forever Fans.*

---

## 📌 Overview

**The Loyalty Project** is a full-stack application built to solve a critical product challenge:
👉 **Customer drop-off after the first use**

By combining **feedback intelligence** and **UI analysis**, the system identifies *why users leave* and provides **actionable solutions** to improve retention.

---

## 🚨 Problem Statement

> Most users don’t leave because your product is bad — they leave because the experience is unclear, confusing, or overwhelming.

Businesses often:

* Guess why users drop off
* Fix the wrong problems
* Miss critical UX gaps

👉 **The real challenge is identifying the exact friction points early.**

---

## 💡 Solution

**The Loyalty Project** removes guesswork by:

* Analyzing customer feedback
* Auditing UI/UX using computer vision
* Generating structured solutions & templates

---

# 🧩 Core Features

---

## 💬 Voice to Value

### *“Every feedback is a clue. We decode it.”*

**Description:**
Stop guessing why customers leave.
**Voice to Value** transforms raw feedback into:

* 📊 Identified issues
* 🧠 Categorized problems
* 🛠 Actionable solutions
* 📋 Ready-to-use templates

👉 Fix what actually hurts — not what you assume does.

---

## 🖼️ First Impressions

### *“See your product the way your customers do — for the first time, every time.”*

**Description:**
A confusing interface is a silent exit door.

**First Impressions** analyzes UI screenshots to detect:

* 🎯 Visual complexity
* 🧱 UI element density
* 🌗 Readability & contrast
* 📱 Layout type (mobile/desktop)

👉 Identify friction points before users leave.

---

# 🎥 Demo Video

👉 Watch the full demo here:
🔗 **[Google Drive Demo Link](https://drive.google.com/file/d/1PiIImiaQHlAbyHx7F64XAUlC_AfCHkf9/view?usp=sharing)**

---

# 📸 Screenshots 
Uploaded in Output folder

---

# 🛠️ Tech Stack

### Frontend

* HTML
* Tailwind CSS
* JavaScript

### Backend

* FastAPI (Python)

### Computer Vision

* OpenCV
* NumPy

---

# 📊 User Research Insights

A survey was conducted among real users (friends & family) to understand why customers drop off after first use.

### 🔍 Key Observations

#### 🧠 1. UI/UX Complexity (Most Common)

Users frequently reported:

* Confusing interfaces
* Cluttered layouts
* Too many features at once

👉 **Insight:** Overwhelming UI leads to immediate drop-off.

---

#### ⚡ 2. Performance & Reliability Issues

* Laggy systems
* Data not saving
* Bugs and glitches

👉 **Insight:** Poor performance quickly breaks user trust.

---

#### 🧭 3. Onboarding & Usability Friction

* Too much setup required
* Difficult navigation
* Not intuitive

👉 **Insight:** If users struggle early, they don’t return.

---

#### 📞 4. Customer Support Gaps

* Poor service experience
* Ineffective chatbots
* Slow support response

👉 **Insight:** Lack of support prevents recovery after a bad experience.

---

#### 💸 5. Value Perception Issues

* Paying for basic features
* Product not matching expectations

👉 **Insight:** Users leave when value is unclear or feels unfair.

---

#### 🌍 6. Product Fit & Alternatives

* Preference for other tools (e.g., Zoom)
* Not suitable for specific needs

👉 **Insight:** Drop-off is sometimes due to poor product-market fit.

---

### 🎯 Conclusion

> Customer drop-off is not caused by a single issue — it is a combination of **UX friction, performance issues, unclear value, and poor support systems**.

---

### 🧩 Impact on This Project

These insights directly influenced the design of:

* 💬 **Voice to Value** → Detects issues from user feedback
* 🖼️ **First Impressions** → Identifies UI/UX problems visually

👉 The system focuses on **detecting real friction points and providing actionable solutions.**

---


# 📂 Project Structure

```id="struct1"
project/
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
├── assets/
│   ├── home.png
│   ├── feedback_output.png
│   ├── ui_output.png
│
└── README.md
```

---

# ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```id="clone1"
git clone <your-repo-link>
cd project
```

---

### 2️⃣ Backend Setup

```id="setup1"
cd Backend
pip install fastapi uvicorn python-multipart opencv-python numpy
```

Run backend:

```id="run1"
uvicorn main:app --reload
```

---

### 3️⃣ Frontend Setup

```id="setup2"
cd Frontend
python -m http.server 5500
```

Open:

```id="open1"
http://127.0.0.1:5500
```

---

# 🔗 API Endpoints

| Endpoint      | Method | Description       |
| ------------- | ------ | ----------------- |
| `/analyze`    | POST   | Feedback analysis |
| `/analyze-ui` | POST   | UI image analysis |

---

# 🧠 How It Works

### Feedback Pipeline

1. Input feedback
2. Keyword detection
3. Issue classification
4. Solution + template generation

---

### UI Analysis Pipeline

1. Upload UI screenshot
2. Image preprocessing
3. Edge detection (complexity)
4. Contour detection (elements)
5. Brightness & layout analysis
6. Insight generation

---

# 🌟 Future Improvements

* Advanced NLP models
* Deep learning-based UI detection
* Real-time analytics dashboard
* SaaS product version

---

# 📦 Repository Description (Use on GitHub)

**Short:**

> Analyze customer drop-off after first use using feedback intelligence and computer vision.

**Detailed:**

> A full-stack application that detects UX issues from customer feedback and UI screenshots using FastAPI and OpenCV, generating actionable insights to improve retention.

---

# 📜 Copyright

© 2026 Sajani M. All rights reserved.

This project is created for educational and evaluation purposes.
Unauthorized use, copying, or distribution is prohibited.

---

# 👤 Author

**Sajani M**
Aspiring AI Engineer | AIML Student

---

