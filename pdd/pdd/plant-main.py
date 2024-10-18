from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:3001",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL = tf.keras.models.load_model("../models/plants.h5")
CLASS_NAMES = [
    "Pepper bell Bacterial_spot",
    "Pepper bell healthy",
    "Potato Early Blight",
    "Potato Late Blight",
    "Potato Healthy",
    "Tomato Bacterial spot",
    "Tomato Early blight",
    "Tomato Late blight",
    "Tomato Leaf Mold",
    "Tomato Sectorial leaf spot",
    "Tomato Spider mites Two spotted spider mite",
    "Tomato Target Spot",
    "Tomato YellowLeaf Curl Virus",
    "Tomato mosaic virus",
    "Tomato healthy",
]


@app.get("/ping")
async def ping():
    return "Hello, I am alive"


def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image


def get_doctor_advice(class_name):
    doctor_info = {"number": None, "name": "", "advice": ""}

    if class_name == "Pepper bell Bacterial_spot":
        doctor_info = {
            "number": "101",
            "name": "Dr. Green",
            "advice": "Use resistant varieties and apply fungicides.",
        }
    elif class_name == "Pepper bell healthy":
        doctor_info = {
            "number": "102",
            "name": "Dr. Fresh",
            "advice": "Maintain good soil health.",
        }
    elif class_name == "Potato Early Blight":
        doctor_info = {
            "number": "201",
            "name": "Dr. Root",
            "advice": "Apply fungicides early and rotate crops.",
        }
    elif class_name == "Potato Late Blight":
        doctor_info = {
            "number": "202",
            "name": "Dr. Sprout",
            "advice": "Remove infected plants and use resistant varieties.",
        }
    elif class_name == "Potato Healthy":
        doctor_info = {
            "number": "203",
            "name": "Dr. Fresh",
            "advice": "Keep monitoring and maintain soil health.",
        }
    elif class_name == "Tomato Bacterial spot":
        doctor_info = {
            "number": "301",
            "name": "Dr. Bloom",
            "advice": "Ensure good airflow and avoid overhead watering.",
        }
    elif class_name == "Tomato Early blight":
        doctor_info = {
            "number": "302",
            "name": "Dr. Ripen",
            "advice": "Use fungicides and crop rotation.",
        }
    elif class_name == "Tomato Late blight":
        doctor_info = {
            "number": "303",
            "name": "Dr. Rot",
            "advice": "Remove infected plants and use resistant varieties.",
        }
    elif class_name == "Tomato Leaf Mold":
        doctor_info = {
            "number": "304",
            "name": "Dr. Shade",
            "advice": "Improve ventilation and avoid excess moisture.",
        }
    elif class_name == "Tomato Sectorial leaf spot":
        doctor_info = {
            "number": "305",
            "name": "Dr. Leafy",
            "advice": "Use fungicides and monitor humidity levels.",
        }
    elif class_name == "Tomato Spider mites Two spotted spider mite":
        doctor_info = {
            "number": "306",
            "name": "Dr. Arachnid",
            "advice": "Use miticides and encourage natural predators.",
        }
    elif class_name == "Tomato Target Spot":
        doctor_info = {
            "number": "307",
            "name": "Dr. Spot",
            "advice": "Apply fungicides and practice crop rotation.",
        }
    elif class_name == "Tomato YellowLeaf Curl Virus":
        doctor_info = {
            "number": "308",
            "name": "Dr. Curl",
            "advice": "Control aphids and remove infected plants.",
        }
    elif class_name == "Tomato mosaic virus":
        doctor_info = {
            "number": "309",
            "name": "Dr. Mosaic",
            "advice": "Remove infected plants and control aphid populations.",
        }
    elif class_name == "Tomato healthy":
        doctor_info = {
            "number": "310",
            "name": "Dr. Healthy",
            "advice": "Maintain good agricultural practices.",
        }
    else:
        doctor_info = {
            "number": "000",
            "name": "Dr. Unknown",
            "advice": "Consult a specialist.",
        }

    return doctor_info


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)
    prediction = MODEL.predict(img_batch)

    predicted_class = CLASS_NAMES[np.argmax(prediction[0])]
    confidence = np.max(prediction[0])

    doctor_info = get_doctor_advice(predicted_class)

    return {
        "class": predicted_class,
        "confidence": float(confidence),
        "doctor_number": doctor_info["number"],
        "doctor_name": doctor_info["name"],
        "advice": doctor_info["advice"],
    }


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
