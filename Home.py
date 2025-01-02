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
description2 = "➡️ Data Engineering and Software Development Enthusiast."
email = "aopandey@purdue.edu"
social_media = {
    "LinkedIn": "https://www.linkedin.com/in/avinashopandey/",
    "GitHub": "https://github.com/Aopandey"
}

# Load Resources
with open("styles/main.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with open("images/Avinash Pandey Resume ML.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open("images/photo.jpg")

# Layout
col1, col2 = st.columns([3, 1], gap="small")

with col1:
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
    #st.write("----")
    st.write("🌟Explore the website to learn more about the projects I've done to demonstrate my skills. "
             "Feel free to contact me!🌟")

with col2:
    st.image(profile_pic)

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
- **Languages:** Python, SQL, R/R-Studio, Java, C++, C, JavaScript, CSS 
- **Framework and Libraries:** Gemini API, Pandas, PyTorch, TensorFlow, LangChain, Haystack, ZenML, Prefect, Tableau, PowerBI, Flask,
Django, PyPDF2, Fitz, GitHub, AWS, Microsoft Azure, React, Redux, Express, PySimpleGUI, Paperetl, GROBID
- **Database Management:**  MySQL, Microsoft SQL Server, Docker, Dagster, MongoDB, Azure Data Studio
""")

# Concepts Learning
st.write("---")
st.subheader("Concepts Learning")
st.write("""
- **Machine Learning Operations (MLOps):** Implementing and managing machine learning pipelines and workflows in production.
- **Cloud Integration:** Learning Docker, Azure, and Dagster for scalable and efficient deployment of applications.
- **Metadata Filtering Algorithms:** Improving precision in summarized research outputs.
- **Automated Data Processing:** Using tools like ZenML and Prefect for efficient data handling.
- **Streamlit Applications:** Developing user-friendly web applications for data visualization and interaction.
- **Frontend Development with React:** Building dynamic and responsive web applications using React.js, including state management with Redux.
- **API Integration:** Connecting frontend applications with backend services through RESTful APIs.
""")

# Work Experience
st.write("---")
st.subheader("Work Experience")
st.write("""
**Machine Learning Engineering Intern**  
*Aider Ventures, Indianapolis, IN*  
*July 2024 – Present*

- Develop automated pipelines using ChromaDB and FAISS Index Embeddings to fetch and summarize trending research papers,
processing and summarizing over 2000 papers, ensuring efficient data handling and information retrieval from icml.cc.
- Engineer scalable data pipelines leveraging Gemini API, ZenML, and Prefect Python to analyze and classify over 10,000 research papers,
enhancing the categorization process of AI and LLM datasets.
- Implement metadata filtering algorithms in LangChain, improving the precision of summarized research outputs by 20%.
- Focus on building scalable, DAG-based pipelines, employing advanced techniques to manage and process large datasets, reducing
processing time by 40%, improving the efficiency of data workflows, and enabling rapid data analysis and decision-making.
- Deploy a Streamlit-based application showcasing the developed application enhancing user engagement and accessibility.

**Business Analyst Intern – Office of Technology Services**  
*Legislative Services Agency, Indianapolis, IN*  
*December 2023 – March 2024*

- Collaborated with software developers to support & troubleshoot critical software, achieving a 95% issue resolution rate.
- Executed advanced data verification and timeliness assurance processes for the Indiana General Assembly, leveraging data analytics
and quality control methodologies to maintain unparalleled data fidelity and promptness with a 98% accuracy rate.
- Facilitated strategic interactions and technical support with Indiana lawmakers and Legislative Services Agency staff, optimizing
business processes through problem resolution and the development of tailored applications and tools.
""")
