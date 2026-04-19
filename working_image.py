import streamlit as st
from google import genai
from dotenv import load_dotenv
import os
from PIL import Image

# Load API key
load_dotenv()
my_api_key = os.getenv("QUIZMAKER_GEMINI_API_KEY")

# Initialize client
client = genai.Client(api_key=my_api_key)

# Upload images
images = st.file_uploader(
    "Upload the photos of your note",
    type=['jpg','jpeg','png'],
    accept_multiple_files=True
)

# Process images
if images:

    pil_images = []

    # convert to PIL
    for img in images:
        pil_img = Image.open(img)
        pil_images.append(pil_img)

    # prompt
    prompt = """Summarize the picture in note format at max 100 words"""

    # Gemini API call
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[pil_images, prompt]
    )

    # display result
    st.markdown(response.text)