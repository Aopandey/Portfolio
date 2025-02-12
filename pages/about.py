import streamlit as st
from PIL import Image, ImageOps


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


    st.markdown("<br><br><br>", unsafe_allow_html=True)

    # Photo Slider Section
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
        # Apply exif_transpose to fix orientation if needed
        img = ImageOps.exif_transpose(img)
        # If image is landscape, rotate it to portrait
        if img.width > img.height:
            img = img.rotate(90, expand=True)
        images.append(img)

    # Create a container that centers the image and slider together
    with st.container():
        # Use columns to limit the slider width.
        # Here, we create three columns with ratios that force the slider to be in a narrow central column.
        col_left, col_center, col_right = st.columns([2, 1, 2])

        # Display the image in the center column.
        image_placeholder = col_center.empty()
        image_placeholder.image(images[0], caption="Photo 1", width=500)

        # Place the slider inside the center column too.
        selected_index = col_center.slider("Select a photo", 0, len(images) - 1, 0, key="photo_slider")

        # Update the image according to the slider selection.
        image_placeholder.image(images[selected_index], caption=f"Photo {selected_index + 1}", width=300)
