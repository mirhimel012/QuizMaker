import streamlit as st
from PIL import Image   # Pic preview 

# App Title
st.title("Note Summary and Quiz Generator")
st.markdown("Upload upto 3 images to generate Note summary and Quizzes")
st.divider()

# Sidebar 
with st.sidebar:
    st.header("Controls")

    # Upload images
    images = st.file_uploader(
        "Upload the photos of your note",
        type=['jpg','jpeg','png'],   
        accept_multiple_files=True   
    )

    # Show uploaded images
    if images:
        if len(images) > 3:
            st.error("Upload at max 3 images")
        else:
            st.subheader("Uploaded images")

            # create columns
            cols = st.columns(len(images))

            # display images
            for i, img in enumerate(images):
                with cols[i]:
                    st.image(img)

    # Difficulty selector
    selected_option = st.selectbox(
        "Enter the difficulty of your quiz",
        ("Easy","Medium","Hard"),
        index=None
    )

    # Action button
    pressed = st.button("Click the button to initiate AI", type="primary")


# Placeholder for future logic
if pressed:
    st.info("AI features will be added in next phase...")