import streamlit as st
from PIL import Image

# --- ABOUT ME PAGE CONTENT ---


def show_about():
    # Title
    st.title("About Me")

    # Brief paragraph about you
    st.write("""
    I am a passionate Data & Machine Learning Engineer with a strong background in computer science and mathematics. 
    I love solving complex problems and developing innovative solutions that leverage cutting-edge technologies to make a difference.
    """)

    # Hobbies section
    st.header("Hobbies")
    st.write("""
    In my free time, I enjoy hiking, photography, and exploring new cultures. 
    Capturing moments with my camera and sharing experiences helps me find balance and fuels my creativity.
    """)

    # Photo Slider Section
    st.header("Personal/Interests Photos")

    # List of image file paths (make sure these files exist in the specified location)
    image_paths = [
        "images/hobby1.JPG",
        "images/hobby2.JPG",
        "images/hobby3.JPG"
    ]

    # Load images using PIL
    images = [Image.open(path) for path in image_paths]

    # Create a slider to select the image index
    selected_index = st.slider("Select a photo", 0, len(images)-1, 0)

    # Display the selected image with a caption
    st.image(images[selected_index], caption=f"Photo {selected_index+1}", use_column_width=True)
