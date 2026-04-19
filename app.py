import streamlit as st
from api_calling import note_generator, quiz_generator
from PIL import Image

# App Title
st.title("Note Summary and Quiz Generator")
st.markdown("Upload upto 3 images to generate Note summary and Quizzes")
st.divider()

# Sidebar for controls
with st.sidebar:
    st.header("Controls")

    # Upload multiple images
    images = st.file_uploader(
        "Upload the photos of your note",
        type=['jpg','jpeg','png'],  # allow image types
        accept_multiple_files=True  # allow multiple upload
    )

    pil_images = []

    # Convert uploaded images to PIL format
    for img in images:
        pil_img = Image.open(img)   # convert to PIL image
        pil_images.append(pil_img)

    # Show uploaded images
    if images:
        if len(images) > 3:
            st.error("Upload at max 3 images")  # validation
        else:
            st.subheader("Uploaded images")
            col = st.columns(len(images))  # create columns

            # display images side-by-side
            for i, img in enumerate(images):
                with col[i]:
                    st.image(img)

    # Select quiz difficulty
    selected_option = st.selectbox(
        "Enter the difficulty of your quiz",
        ("Easy","Medium","Hard"),
        index=None
    )

    # Button to start AI
    pressed = st.button("Click the button to initiate AI", type="primary")


# Run AI after button click
if pressed:

    # Check required inputs
    if not images:
        st.error("You must upload 1 image")
    if not selected_option:
        st.error("You must select a difficulty")

    if images and selected_option:

        # NOTE GENERATION
        with st.container(border=True):
            st.subheader("Your note")

            # Loading spinner
            with st.spinner("AI is writing notes for you"):
                generated_notes = note_generator(pil_images)  # call AI
                st.markdown(generated_notes)  # show note


        # QUIZ GENERATION
        with st.container(border=True):
            st.subheader(f"Quiz ({selected_option}) Difficulty")

            with st.spinner("AI is generating the quizzes"):
                quizzes = quiz_generator(pil_images, selected_option)
                st.markdown(quizzes)  # show quiz