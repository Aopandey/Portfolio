import streamlit as zx
import pandas
import base64
from pathlib import Path
from PIL import Image

title = "Portfolio | Avinash Pandey"
name = "Avinash Pandey"
description1 = ("➡️ Senior Computer Science Student with a minor in Mathematics at Purdue University"
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
- Framework and Libraries: LangChain, Haystack, ZenML, Prefect, React, Redux, Express, Django, 
    Flask, PySimpleGUI, Pandas, Paperetl, GROBID, PyTorch, TensorFlow, GitHub, AWS, Microsoft Azure, 
    PyCharm, Jupyter
- Database Management: MySQL, MongoDB, Microsoft SQL Server, Azure Data Studio
""")

# Concepts Learning
zx.write("#")
zx.subheader("Concepts Learning")
zx.write("---")
zx.write("""
- Advanced Data Pipelines: Building scalable, DAG-based pipelines to manage and process large datasets.
- Metadata Filtering Algorithms: Improving precision in summarized research outputs.
- Automated Data Processing: Using tools like ZenML and Prefect for efficient data handling.
- Streamlit Applications: Developing user-friendly web applications for data visualization and interaction.
""")

# Work Experience
zx.write("#")
zx.subheader("Work Experience")
zx.write("---")
zx.write("""
**Machine Learning Engineering Intern**  
Aider Ventures, Indianapolis, IN  
*July 2024 – Present*

- Developed automated pipelines using Haystack to fetch and summarize trending research papers.
- Engineered scalable data pipelines leveraging ZenML and Prefect Python to analyze and classify research papers.
- Implemented metadata filtering algorithms in LangChain, improving the precision of summarized research outputs.
- Built scalable, DAG-based pipelines for large dataset processing.
- Deployed a Streamlit-based application to showcase the developed application.

**Business Analyst Intern – Office of Technology Services**  
Legislative Services Agency, Indianapolis, IN  
*December 2023 – March 2024*

- Collaborated with software developers to support & troubleshoot critical software.
- Executed advanced data verification and timeliness assurance processes for the Indiana General Assembly.
- Facilitated strategic interactions and technical support with Indiana lawmakers and Legislative Services Agency staff.
""")
