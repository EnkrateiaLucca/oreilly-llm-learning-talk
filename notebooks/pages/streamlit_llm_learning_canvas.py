import streamlit as st
from streamlit_drawable_canvas import st_canvas
import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd
import base64
import requests
import os

API_KEY = os.environ["OPENAI_API_KEY"]
# Helper functions

def save_image(image_data, image_file_path='drawing.png'):
    # Convert the image data to PIL image
    pil_image = Image.fromarray(image_data.astype('uint8'))

        # Save the PIL image to file
    pil_image.save(image_file_path)

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def ask_gpt4_vision(prompt, base64_image):
    headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {API_KEY}"
}

    payload = {
    "model": "gpt-4-vision-preview",
    "messages": [
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": prompt
            },
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
            }
        ]
        }
    ],
    "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    output = response.json()["choices"][0]["message"]["content"]
    
    return output



# Set page config
st.set_page_config(page_title="Drawing App", layout="wide")
# Sidebar
st.sidebar.header("Drawing Options")
draw_mode = st.sidebar.selectbox("Draw Mode", ("freedraw", "line", "rect", "circle", "transform"))
stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 3)
stroke_color = st.sidebar.color_picker("Stroke color hex: ")
bg_color = st.sidebar.color_picker("Background color hex: ", "#eee")
bg_image = st.sidebar.file_uploader("Background image:", type=["png", "jpg"])

# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    background_image=bg_image,
    update_streamlit=True,
    width=800,
    height=400,
    drawing_mode=draw_mode,
    key="canvas",
)



if st.button('Save'):
    # Save the image data
    if canvas_result.image_data is not None:
        save_image(canvas_result.image_data)
        

if st.button("AI"):
    # AI
    ai_input_image_path = 'ai_input_image.png'
    save_image(canvas_result.image_data, image_file_path=ai_input_image_path)
    base64_image = encode_image(ai_input_image_path)
    prompt = "What is this image?"
    response = ask_gpt4_vision(prompt, base64_image)
    st.write(response)
