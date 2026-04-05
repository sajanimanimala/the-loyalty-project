from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import shutil
from analyzer import analyze_feedback, analyze_image

app = FastAPI()

# CORS - allows to safely access resources from other domains
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "API is running"}
# FEEDBACK ANALYSIS (text)
@app.post("/analyze")
async def analyze(feedback: str = Form(...)):
    result = analyze_feedback(feedback)
    return {
        "analysis": result
    }
# UI ANALYSIS (image only)
@app.post("/analyze-ui")
async def analyze_ui(image: UploadFile = File(...)):

    image_path = f"temp_{image.filename}"

    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    insights = analyze_image(image_path)

    return {
        "image_insights": insights
    }
