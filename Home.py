import streamlit as st
import pandas as pd
import base64
from pathlib import Path
from PIL import Image

# Page Configuration
title = "Portfolio | Avinash Pandey"
st.set_page_config(page_title=title)

# Personal Information
name = "Avinash Pandey"
description1 = ("➡️ Senior Computer Science Student with a minor in Mathematics at Purdue University"
                ", Graduating December 2024.")
description2 = "➡️ Software Development and Data Science Enthusiast."
email = "aopandey@purdue.edu"
social_media = {
    "LinkedIn": "https://www.linkedin.com/in/avinashopandey/",
    "GitHub": "https://github.com/Aopandey"
}

# Load Resources
with open("styles/main.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with open("images/Resume Avinash Pandey.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open("images/photo.jpg")

# Layout
col1, col2 = st.columns([3, 1], gap="small")

with col1:
    st.image(profile_pic)

with col2:
    st.title(name)
    st.write(description1)
    st.write(description2)
    st.download_button(
        label="📁 Download Resume",
        data=PDFbyte,
        file_name="Avinash Pandey Resume.pdf",
        mime="application/octet-stream",
    )
    st.write(f"📧 Email: {email}")
    st.write("---")
    st.write("🌟Explore the website to learn more about the projects I've done to demonstrate my skills. "
             "Feel free to contact me!🌟")

# Social Media Links
st.write("---")
st.subheader("Professional Platforms")
cols = st.columns(len(social_media))
for index, (platform, link) in enumerate(social_media.items()):
    cols[index].write(f"💻[{platform}]({link})")

# Technical Skills
st.write("---")
st.subheader("Technical Skills")
st.write("""
- **Languages:** Python, C, C++, JavaScript, CSS, Java, R/R-Studio, SQL
- **Framework and Libraries:** LangChain, Haystack, ZenML, Prefect, React, Redux, Express, Django, 
  Flask, PySimpleGUI, Pandas, Paperetl, GROBID, PyTorch, TensorFlow, GitHub, AWS, Microsoft Azure, 
  PyCharm, Jupyter
- **Database Management:** MySQL, MongoDB, Microsoft SQL Server, Azure Data Studio
""")

# Concepts Learning
st.write("---")
st.subheader("Concepts Learning")
st.write("""
- **Advanced Data Pipelines:** Building scalable, DAG-based pipelines to manage and process large datasets.
- **Metadata Filtering Algorithms:** Improving precision in summarized research outputs.
- **Automated Data Processing:** Using tools like ZenML and Prefect for efficient data handling.
- **Streamlit Applications:** Developing user-friendly web applications for data visualization and interaction.
""")

# Work Experience
st.write("---")
st.subheader("Work Experience")
st.write("""
**Machine Learning Engineering Intern**  
*Aider Ventures, Indianapolis, IN*  
*July 2024 – Present*

- Developed automated pipelines using Haystack to fetch and summarize trending research papers.
- Engineered scalable data pipelines leveraging ZenML and Prefect Python to analyze and classify research papers.
- Implemented metadata filtering algorithms in LangChain, improving the precision of summarized research outputs.
- Built scalable, DAG-based pipelines for large dataset processing.
- Deployed a Streamlit-based application to showcase the developed application.

**Business Analyst Intern – Office of Technology Services**  
*Legislative Services Agency, Indianapolis, IN*  
*December 2023 – March 2024*

- Collaborated with software developers to support & troubleshoot critical software.
- Executed advanced data verification and timeliness assurance processes for the Indiana General Assembly.
- Facilitated strategic interactions and technical support with Indiana lawmakers and Legislative Services Agency staff.
""")
