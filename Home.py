import streamlit as zx
import pandas
import base64
from pathlib import Path
from PIL import Image

title = "Portfolio | Avinash Pandey"
name = "Avinash Pandey"
description1 = ("➡️ Senior Computer Science Student with a minor in Mathematics at Purdue University Indianapolis"
                ", Graduating December 2024.")
description2 = "➡️ Software Development and Data Science Enthusiast."
email = "aopandey@purdue.edu"
social_media = {
    "LinkedIn": "https://www.linkedin.com/in/avinashopandey/",
    "GitHub": "https://github.com/Aopandey"
}

zx.set_page_config(page_title=title)

with open("styles/main.css") as f:
    zx.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open("images/Resume Avinash Pandey.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()
    profile_pic = Image.open("images/photo.jpg")

col1, col2 = zx.columns(2, gap="small")
with col1:
    zx.image(profile_pic)

with col2:
    zx.title(name)
    zx.write(description1)
    zx.write(description2)
    zx.download_button(
        label="📁 Download Resume",
        data=PDFbyte,
        file_name="Avinash Pandey Resume.pdf",
        mime="application/octet-stream",
    )
    zx.write("Email:", email)
    zx.write("#")
    zx.write("🌟Explore the website to learn more about the projects I've done to demonstrate my Skills. "
                 "Feel free to contact me!🌟")

zx.write("#")
zx.subheader("Professional Platforms")
zx.write("---")
cols = zx.columns(len(social_media))
for index, (platform, link) in enumerate(social_media.items()):
    cols[index].write(f"💻[{platform}]({link})")

zx.write("#")
zx.subheader("Technical Skills")
zx.write("---")
zx.write("""
    - Languages: Python, C, C++, JavaScript, CSS, Java, R/R-Studio, SQL
    - Framework and Libraries: React, Redux, Express, Django, Flask, PySimpleGUI, Pandas 
    - Tools/Frameworks: GitHub, AWS, Microsoft Azure, PyCharm, Jupyter
    - Database Management: MySQL, MongoDB, Microsoft SQL Server, Azure Data Studio
    """)
