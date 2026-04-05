import json
import os
import cv2
import numpy as np

# Load JSON safely
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "templates_data.json")

with open(file_path, "r") as f:
    data = json.load(f)


# IMAGE ANALYZER
def analyze_image(image_path):
    insights = []

    img = cv2.imread(image_path)

    if img is None:
        return ["Unable to analyze image"]

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Resize for consistency
    gray = cv2.resize(gray, (300, 300))

    # Edge detection (ONLY ONCE)
    edges = cv2.Canny(gray, 50, 150)

    edge_pixels = np.sum(edges > 0)
    total_pixels = edges.size
    edge_density = edge_pixels / total_pixels

    if edge_density > 0.15:
        insights.append("High UI complexity → cluttered interface")
    elif edge_density > 0.05:
        insights.append("Moderate UI complexity → balanced layout")
    else:
        insights.append("Simple UI → clean design")

    # Contours
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contour_count = len(contours)

    if contour_count > 150:
        insights.append("Too many UI elements → overwhelming")
    elif contour_count > 50:
        insights.append("Moderate UI components")
    else:
        insights.append("Minimal UI → easy navigation")

    # Brightness
    brightness = np.mean(gray)

    if brightness < 80:
        insights.append("Dark interface → check readability")
    elif brightness > 180:
        insights.append("Very bright interface → check contrast")
    else:
        insights.append("Balanced brightness")

    # 🔹 Layout
    h, w = gray.shape
    if h > w:
        insights.append("Mobile layout detected")
    else:
        insights.append("Desktop layout detected")

    return insights


# FEEDBACK ANALYZER (MATCH FRONTEND STRUCTURE)
def analyze_feedback(feedback):
    feedback = feedback.lower()

    detected_issues = []

    for category, details in data.items():
        for keyword in details["keywords"]:
            if keyword in feedback:
                detected_issues.append(category)
                break

    detected_issues = list(set(detected_issues))

    # fallback
    if not detected_issues:
        detected_issues.append("value_unclear")

    issues_output = []

    for issue in detected_issues:
        issues_output.append({
            "issue": issue,
            "solutions": data[issue]["solutions"],
            "template": data[issue]["template"]
        })

    # RETURN STRUCTURE MATCHES FRONTEND
    return {
        "issues": issues_output,
        "image_insights": []
    }
