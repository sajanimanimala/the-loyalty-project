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
🔗 **[Google Drive Demo Link](PASTE_YOUR_DRIVE_LINK_HERE)**

---

# 📸 Screenshots

*(Add your screenshots in an `/assets` folder and link them below)*

### 🏠 Home Page

```id="img1"
![Home](assets/home.png)
```

### 💬 Feedback Analysis Output

```id="img2"
![Feedback](assets/feedback_output.png)
```

### 🖼️ UI Analysis Output

```id="img3"
![UI Analysis](assets/ui_output.png)
```

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

