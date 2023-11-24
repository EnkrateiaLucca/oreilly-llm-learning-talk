import wget
import streamlit as st
from openai import OpenAI
from PIL import Image
import numpy as np
import os
import base64

if 'filename' not in st.session_state:
    st.session_state['filename'] = []

st.title("DALL-E: Creating Images from Text")

client = OpenAI()

# Define grid size and block size
num_rows = st.sidebar.number_input("Number of Rows", min_value=1, max_value=10, value=3)
num_cols = st.sidebar.slider("Number of Columns", min_value=1, max_value=10, value=3)
block_width = st.sidebar.slider("Block Width", min_value=100, max_value=500, value=200)
block_height = st.sidebar.slider("Block Height", min_value=100, max_value=500, value=200)

# User input for grid location
selected_row = st.number_input("Select Row", min_value=0, max_value=num_rows-1, value=0)
selected_col = st.number_input("Select Column", min_value=0, max_value=num_cols-1, value=0)
prompt = st.text_input("Enter the prompt")

# Create the columns for the grid
grid_columns = [st.columns(num_cols) for _ in range(num_rows)]

# Initialize placeholders for the grid
grid_placeholders = [[None for _ in range(num_cols)] for _ in range(num_rows)]

# Assign a placeholder to each cell in the grid
for i in range(num_rows):
    for j in range(num_cols):
        with grid_columns[i][j]:
            grid_placeholders[i][j] = st.empty()
            grid_placeholders[i][j].image(np.random.uniform(0, 1, (block_width, block_height, 3)), width=block_width)


if st.button("Generate Image"):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url
    st.session_state["filename"].append(f"images/output_image_{selected_row}_{selected_col}.png")

    wget.download(image_url, st.session_state["filename"][-1])


# Update the image in the correct placeholder
if len(st.session_state["filename"])!=0:
    for i in range(len(st.session_state["filename"])):
        st.write(st.session_state["filename"])    
        image = Image.open(st.session_state["filename"][i])
        image = image.resize((block_width, block_height))
        placeholder = grid_placeholders[selected_row][selected_col]
        placeholder.image(image)