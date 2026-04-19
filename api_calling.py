from google import genai
from dotenv import load_dotenv
import os, io

# Load .env file
load_dotenv()

# Get API key
my_api_key = os.getenv("QUIZMAKER_GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=my_api_key)


# NOTE GENERATOR
def note_generator(images):

    # prompt for AI
    prompt = """Summarize the picture in note format in language Bangla at max 100 words
    make sure to add necessary markdown to differentiate different section"""

    # call Gemini API
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images, prompt]
    )

    return response.text


# QUIZ GENERATOR
def quiz_generator(image, difficulty):

    # prompt for quiz
    prompt = f"Generate 3 quizzes based on the {difficulty}. Add correct answer also."

    # call Gemini API
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[image, prompt]
    )

    return response.text