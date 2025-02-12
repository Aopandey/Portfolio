import streamlit as st
from PIL import Image, ImageOps


def show_about():
    # Title and About Me text (centered)
    col_center, _ = st.columns([1, 3])
    with col_center:
        st.title("About Me")
    st.write("""
    I am a passionate Data & Machine Learning Engineer with a strong background in computer science and mathematics. 
    I love solving complex problems and developing innovative solutions that leverage cutting-edge technologies to make a difference.
    """)

    # Hobbies section (centered)
    col_center, _ = st.columns([1, 3])
    with col_center:
        st.header("Hobbies")
    st.write("""
    In my free time, I enjoy hiking, photography, and exploring new cultures. 
    Capturing moments with my camera and sharing experiences helps me find balance and fuels my creativity.
    """)

    # Personal/Interests Photos Section
    col_center, _ = st.columns([1, 3])
    with col_center:
        st.header("Personal/Interests Photos")

    # List of image file paths (ensure these files exist in the specified location)
    image_paths = [
        "images/hobby1.JPG",
        "images/hobby2.JPG",
        "images/hobby3.JPG"
    ]

    # Load images using PIL and force portrait orientation:
    images = []
    for path in image_paths:
        img = Image.open(path)
        # Use ImageOps.exif_transpose to correct orientation (if EXIF data is available)
        img = ImageOps.exif_transpose(img)
        # If the image is landscape, rotate it 90 degrees to make it portrait
        if img.width > img.height:
            img = img.rotate(90, expand=True)
        images.append(img)

    # Use a container to center the photo and slider together.
    with st.container():
        # Create two columns so we can center the image (by putting it in the middle column)
        col_left, col_center, col_right = st.columns([1, 2, 1])
        # The image is displayed in the center column.
        # Use a fixed width (for example, 300 pixels) to ensure it doesn't span the entire page.
        with col_center:
            # Use a placeholder so the image updates when the slider value changes.
            image_placeholder = st.empty()

        # Now, below the image, display the slider.
        # Note: We use the slider's value to index the images list.
        selected_index = st.slider("Select a photo", 0, len(images) - 1, 0, key="photo_slider")

        # Now update the placeholder with the selected image.
        with col_center:
            image_placeholder.image(images[selected_index], caption=f"Photo {selected_index + 1}", width=300)
