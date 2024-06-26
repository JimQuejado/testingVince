import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from PIL import Image, ImageOps
import os

# Load model
model_path = 'model.h5'
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at {model_path}")

model = load_model(model_path)

    
# Streamlit app
st.title("Image Classification with MobileNet")
st.write("Upload an image for classification")


file = st.file_uploader("", type=["jpg", "png"])
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


def import_and_predict(image_data, model):
    size = (224, 224)
    image = ImageOps.fit(image_data, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    return prediction

if uploaded_file is not None:
    image = Image.open(file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("Classifying...")

    prediction = prepare_image_and_predict(image, model)
    
    try:
        class_names = ["Bishop", "King", "Knight", "Pawn", "Queen", "Rook"]
        pred_class = np.argmax(prediction, axis=1)[0]

        st.write(f"Image is a {class_names[pred_class]}")
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
