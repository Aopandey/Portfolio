import streamlit as st
from PIL import Image, ImageOps


def show_about():
    # Title
    st.title("About Me")
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <span style='font-size:1.1em;'>
    I wear multiple hats—part engineer, part problem solver. My journey from <span style='color:#1E90FF; font-weight:bold;'>India to Indiana</span> has been one of growth, resilience, and discovery, leading me to specialize in <span style='color:#FF6347; font-weight:bold;'>AI-driven data pipelines</span>, <span style='color:#FF6347; font-weight:bold;'>machine learning</span>, and <span style='color:#FF6347; font-weight:bold;'>data engineering</span>. On the technical front, I build scalable ETL pipelines, optimize AI retrieval models, and design interactive data visualizations. The data-driven side of me focuses on structuring unstructured data, improving model accuracy, and bridging the gap between AI and business strategy.
    <br>
    My academic journey reflects my curiosity and adaptability. I earned a Bachelor’s degree in <span style='color:#1E90FF; font-weight:bold;'>Computer Science</span> with a <span style='color:#1E90FF; font-weight:bold;'>Minor in Mathematics</span> from <span style='color:#1E90FF; font-weight:bold;'>Purdue University</span>, an achievement that once felt like a distant dream. Originally starting in Computer Engineering, I soon realized that Computer Science was my true passion, leading me to pivot and explore AI, data engineering, and large-scale data processing.
    <br><br>
    <span style='color:#1E90FF; font-size:1em; font-weight:bold;'>Leadership & Projects</span>
    <br><br>
    - Co-founded the Computer Science Club at Purdue Indianapolis, increasing engagement by <span style='color:#FF6347; font-weight:bold;'>100%</span> and organizing hackathons with <span style='color:#FF6347; font-weight:bold;'>200+ participants</span>.
    <br>
    - Mentored <span style='color:#FF6347; font-weight:bold;'>50+ international students</span> through Purdue’s International Peer Mentoring Program, fostering an inclusive environment.
    <br>
    - Interned at <span style='color:#1E90FF; font-weight:bold;'>Aider Ventures</span>, where I developed scalable pipelines and interactive dashboards to analyze <span style='color:#FF6347; font-weight:bold;'>10,000+ research papers</span>.
    <br>
    - Worked as a Business Analyst Intern at the <span style='color:#1E90FF; font-weight:bold;'>Legislative Services Agency</span>, supporting Indiana lawmakers with technical solutions.
    <br>
    - Lost over <span style='color:#FF6347; font-weight:bold;'>100 pounds</span> in two years, reinforcing my belief in discipline, consistency, and resilience.
    <br><br>
    I thrive at the intersection of AI, data, and real-world impact, always looking for ways to turn complex problems into practical, scalable solutions.
    </span>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # Hobbies section
    st.title("Hobbies and Interests")
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <span style='font-size:1.1em;'>
    Beyond my work in AI and data science, I have a deep love for sports, creativity, and adventure. You’ll often find me:
    <br><br>
    - <strong>⚽ Playing or watching soccer (football)</strong> — a lifelong passion, always cheering for <span style='color:#FF6347; font-weight:bold;'>Messi &amp; Barcelona</span>.
    <br>
    - <strong>🏋️ Working out</strong> — fitness has been a huge part of my journey, helping me develop discipline and focus.
    <br>
    - <strong>🎮 Diving into video games</strong> — from immersive story-driven RPGs to fast-paced FPS games.
    <br>
    - <strong>⛰️ Hiking &amp; bouldering</strong> — always looking for new trails and climbing routes to challenge myself.
    <br>
    - <strong>🎬 Watching anime &amp; Star Wars</strong> — whether it’s the latest Shonen series or a rewatch of <span style='color:#FF6347; font-weight:bold;'>The Mandalorian</span>.
    <br>
    - <strong>👟 Collecting sneakers</strong> — because a fresh pair of kicks is always a good idea.
    <br>
    - <strong>🎵 Listening to music (rap &amp; hip-hop)</strong> — <span style='color:#FF6347; font-weight:bold;'>Kanye, Kendrick</span> and classic 2000s beats keep me inspired.
    <br><br>
    No matter what I’m doing—whether coding, climbing, or competing—I bring the same energy: a drive to push boundaries, learn, and grow.
    </span>
    """, unsafe_allow_html=True)


    st.markdown("<br><br><br>", unsafe_allow_html=True)

    # --- Photo Slider Section ---
    # List of image file paths (ensure these files exist in the specified location)
    image_paths = [
        "images/hobby1.JPG",
        "images/hobby2.JPG",
        "images/hobby3.JPG",
        "images/hobby4.jpg",
        "images/hobby5.JPG",
        "images/hobby6.JPG",
        "images/hobby7.jpg"
    ]

    # Specify which images should remain in their original (landscape) orientation.
    landscape_exceptions = ["images/hobby3.JPG", "images/hobby7.jpg"]

    # Load images using PIL and force portrait orientation (except for exceptions):
    images = []
    for path in image_paths:
        img = Image.open(path)
        img = ImageOps.exif_transpose(img)  # Correct orientation if EXIF is available
        if path not in landscape_exceptions and img.width > img.height:
            img = img.rotate(90, expand=True)
        images.append(img)

    # Place the slider inside a container with columns to shift it to the right.
    with st.container():
        # Adjust the column ratios to move the slider toward the right.
        col_slider_left, col_slider_center, col_slider_right = st.columns([1, 1, 2])
        with col_slider_center:
            # Slider now ranges from 1 to len(images). We'll subtract 1 to use it as an index.
            selected_number = st.slider("Select a photo", 1, len(images), 1, key="photo_slider")
    selected_index = selected_number - 1

    # Center the image in a container.
    with st.container():
        col_left, col_center, col_right = st.columns([2, 1, 2])
        with col_center:
            st.image(images[selected_index], caption=f"Photo {selected_number}", width=600)
