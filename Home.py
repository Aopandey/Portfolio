# import streamlit as st
# import pandas as pd
# import base64
# from pathlib import Path
# from PIL import Image
#
# # Page Configuration
# title = "Portfolio | Avinash Pandey"
# st.set_page_config(page_title=title)
#
# # Personal Information
# name = "Avinash Pandey"
# description1 = ("➡️ Computer Science Graduate with a minor in Mathematics from Purdue University"
#                 ", Graduated December 2024.")
# description2 = "➡️ AI Engineering and Data Engineering Enthusiast."
# email = "aopandey24@gmail.com"
# social_media = {
#     "LinkedIn": "https://www.linkedin.com/in/avinashopandey/",
#     "GitHub": "https://github.com/Aopandey"
# }
#
# # Load Resources
# with open("styles/main.css") as f:
#     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
#
# with open("images/Avinash Pandey Resume DS.pdf", "rb") as pdf_file:
#     PDFbyte = pdf_file.read()
#
# profile_pic = Image.open("images/photo.jpg")
#
# # Layout
# col1, col2 = st.columns([3, 1], gap="small")
#
# with col1:
#     st.title(name)
#     st.write(description1)
#     st.write(description2)
#     st.download_button(
#         label="📁 Download Resume",
#         data=PDFbyte,
#         file_name="Avinash Pandey Resume.pdf",
#         mime="application/octet-stream",
#     )
#     st.write(f"📧 Email: {email}")
#     #st.write("----")
#     st.write("🌟Explore the website to learn more about the projects I've done to demonstrate my skills. "
#              "Feel free to contact me!🌟")
#
# with col2:
#     st.image(profile_pic)
#
# # Social Media Links
# st.write("---")
# st.subheader("Professional Platforms")
# cols = st.columns(len(social_media))
# for index, (platform, link) in enumerate(social_media.items()):
#     cols[index].write(f"💻[{platform}]({link})")
#
# # Technical Skills
# st.write("---")
# st.subheader("Technical Skills")
# st.write("""
# - **Programming and Data management:** Python, SQL, R, Java, C++, JavaScript, SQL Server, ETL Pipelines
# - **Frameworks and Tools:** TensorFlow, PyTorch, Scikit-learn, Django, Pandas, NumPy, Tableau, Power BI, Git, GitHub
# - **Cloud and Big Data:** AWS (S3, Lambda, EC2), Azure Data Lake, Hadoop, Spark, Docker, Dagster
# - **Machine Learning and AI:** OpenAI API, Gemini API, LangChain, Hugging Face, FAISS, ChromaDB, ZenML, Haystack
# """)
#
# # Work Experience
# st.write("---")
# st.subheader("Work Experience")
# st.write("""
# **Machine Learning Engineering Intern**
# *Aider Ventures, Indianapolis, IN*
# *July 2024 – Present*
#
# - Developed automated data pipelines using FAISS embeddings and ChromaDB to summarize over 2,600 research papers from
# ICML 2024, optimizing data handling and ensuring accurate information extraction from scraped source icml.cc
# - Engineered scalable pipelines leveraging Gemini API to process and classify over 10,000 research papers, improving the
# categorization process of datasets and increasing system efficiency by 40% through data processing techniques
# - Implemented metadata filtering algorithms in LangChain, improving precision of summarized research outputs by 20%
# - Constructed an interactive dashboard for visualizing and analyzing key insights like the number of papers by university and
# top research areas, enabling non-technical professionals to get insightful trends across over 10,000 papers
#
#
# **Business Analyst Intern – Office of Technology Services**
# *Legislative Services Agency, Indianapolis, IN*
# *December 2023 – March 2024*
#
# - Collaborated with Software Developers and Business Analysts to support and troubleshoot internal software using tools like
# Tableau, SQL Server, and Power BI, achieving a 95% resolution rate
# - Executed data verification processes through ETL pipelines, ensuring 98% accuracy for Indiana General Assembly datasets
# - Facilitated strategic interactions and technical support with Indiana lawmakers and Legislative Services Agency staff,
# optimizing business processes through the development of tailored applications and problem resolution tools
# """)

import streamlit as st
from PIL import Image

# --- PAGE CONFIGURATION (Use wide layout so the header can span full width) ---
st.set_page_config(page_title="Portfolio | Avinash Pandey", layout="wide")

# --- LOAD GLOBAL CSS (Your Provided Styles) ---
with open("styles/main.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- ADDITIONAL CUSTOM CSS ---
st.markdown("""
    <style>
    /* Smaller download buttons */
    div.stDownloadButton > button {
        padding: 0.25em 0.5em;
        font-size: 0.8em;
    }
    </style>
    """, unsafe_allow_html=True)

# --- PERSONAL INFORMATION (Header Section) ---
name = "Avinash Pandey"
description1 = ("""I have a strong curiosity for leveraging AI, Machine Learning, and Data Engineering to develop scalable data pipelines, optimize AI-driven workflows, and extract meaningful insights from unstructured data.

Most recently, as a Machine Learning Engineering Intern at Aider Ventures (Nienna Lab), I developed an automated ETL pipeline that processed 10,000+ research papers, leveraging FAISS embeddings, ChromaDB, and LangChain to improve retrieval accuracy and metadata extraction by 20%. I also built interactive data visualization frameworks to analyze trends in AI research, providing structured insights for non-technical stakeholders.

Previously, at Legislative Services Agency, I designed SQL-based ETL workflows to validate Indiana General Assembly datasets, achieving 98% data accuracy. I collaborated with business analysts to develop Tableau and Power BI dashboards, enhancing legislative data accessibility and decision-making.

In my AI & Data Science projects, I have developed predictive analytics models, including an AI-driven diabetes prediction pipeline that achieved 97% recall and 95% ROC AUC, optimizing feature engineering with SMOTE and deep learning architectures. Additionally, I built an NLP-powered mutual learning framework for news classification, integrating Multinomial Naïve Bayes, SVMs, and neural networks, achieving 98% accuracy.

My expertise encompasses building AI-driven data solutions, developing scalable ETL workflows, and applying advanced analytics to real-world challenges. I excel at bridging business and data science, transforming data-driven questions into production-ready AI applications, and delivering insights that drive strategic decision-making.""")
social_media = {
    "Email": "aopandey24@gmail.com",
    "LinkedIn": "https://www.linkedin.com/in/avinashopandey/",
    "GitHub": "https://github.com/Aopandey"
}

# --- LOAD RESOURCES ---
with open("images/Avinash Pandey Resume DS.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()
with open("images/Avinash Pandey Resume DE.pdf", "rb") as pdf_file:
    PDFbyte1 = pdf_file.read()
with open("images/Avinash Pandey Resume SWE.pdf", "rb") as pdf_file:
    PDFbyte2 = pdf_file.read()

profile_pic = Image.open("images/photo.jpg")

# --- HEADER SECTION (FULL WIDTH) ---
# Create two columns so that the header spans the full page width.
# Left column: Name and photo (stacked)
# Right column: Description (aligned at the top)
col_left, col_right = st.columns([1, 2])
with col_left:
    st.markdown("<h1 style='text-align: center;'>{}</h1>".format(name), unsafe_allow_html=True)
    spacer, image_col = st.columns([1, 3])
    with image_col:
        st.image(profile_pic, width=300)
with col_right:
    st.markdown("<div style='margin-left: -40px; margin-top: 70px;'>{}</div>".format(description1), unsafe_allow_html=True)

# --- NARROW CONTENT AREA (Using Columns) ---
# Create three columns: left spacer, center content, and right spacer.
left_spacer, content_col, right_spacer = st.columns([1, 4, 1])

with content_col:
    # RESUME SECTION
    st.write("---")
    st.subheader("Resume")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.download_button(
            label="📁 Data Science and Analysis Resume",
            data=PDFbyte,
            file_name="Avinash_Pandey_Resume_DS.pdf",
            mime="application/octet-stream"
        )
    with col2:
        st.download_button(
            label="📁 Data Engineering and Pipeline Resume",
            data=PDFbyte1,
            file_name="Avinash_Pandey_Resume_DE.pdf",
            mime="application/octet-stream"
        )
    with col3:
        st.download_button(
            label="📁 Software Engineering Resume",
            data=PDFbyte2,
            file_name="Avinash_Pandey_Resume_SWE.pdf",
            mime="application/octet-stream"
        )

    # PROFESSIONAL PLATFORMS SECTION
    st.write("---")
    st.subheader("Professional Platforms")
    platform_cols = st.columns(len(social_media))
    for idx, (platform, link) in enumerate(social_media.items()):
        platform_cols[idx].write(f"💻 [{platform}]({link})")

    # TECHNICAL SKILLS SECTION
    st.write("---")
    st.subheader("Technical Skills")
    st.write("""
    - **Programming Languages & Development:** Python, Java, C++, JavaScript, TypeScript, R, Flask, FastAPI, Django, Node.js, ReactJS
    - **Data Science & AI Development:**
      - *Machine Learning:* Scikit-learn, XGBoost, PyTorch, TensorFlow, Spark MLlib
      - *Deep Learning:* Multi-Model Learning, Transfer Learning, Representation Learning, NLP (Text Classification, Sentiment Analysis, Named Entity Recognition, Topic Modeling)
      - *AI & Data Science Applications:* Predictive Analytics, Time Series Forecasting, Anomaly Detection, Customer Segmentation
    - **Cloud and Big Data:** AWS (S3, Lambda, EC2), Azure Data Lake, Hadoop, Spark, Docker, Dagster
    - **Machine Learning and AI:** OpenAI API, Gemini API, LangChain, Hugging Face, FAISS, ChromaDB, ZenML, Haystack
    """)

    # WORK EXPERIENCE SECTION
    st.write("---")
    st.subheader("Work Experience")
    st.write("""
    **Machine Learning Engineering Intern**  
    *Aider Ventures, Indianapolis, IN*  
    *July 2024 – Present*

    - Developed automated data pipelines using FAISS embeddings and ChromaDB to summarize over 2,600 research papers from ICML 2024, optimizing data handling and ensuring accurate information extraction from scraped source icml.cc.
    - Engineered scalable pipelines leveraging Gemini API to process and classify over 10,000 research papers, improving the categorization process of datasets and increasing system efficiency by 40% through data processing techniques.
    - Implemented metadata filtering algorithms in LangChain, improving precision of summarized research outputs by 20%.
    - Constructed an interactive dashboard for visualizing and analyzing key insights like the number of papers by university and top research areas, enabling non-technical professionals to gain insightful trends across over 10,000 papers.

    **Business Analyst Intern – Office of Technology Services**  
    *Legislative Services Agency, Indianapolis, IN*  
    *December 2023 – March 2024*

    - Collaborated with Software Developers and Business Analysts to support and troubleshoot internal software using tools like Tableau, SQL Server, and Power BI, achieving a 95% resolution rate.
    - Executed data verification processes through ETL pipelines, ensuring 98% accuracy for Indiana General Assembly datasets.
    - Facilitated strategic interactions and technical support with Indiana lawmakers and Legislative Services Agency staff, optimizing business processes through the development of tailored applications and problem resolution tools.
    """)

# import streamlit as st
#
# # Set Page Configurations
# st.set_page_config(page_title="Avinash Pandey - Portfolio", layout="wide")
#
# # Navigation Bar
# st.markdown("""
#     <style>
#         .nav-bar {
#             display: flex;
#             justify-content: center;
#             gap: 40px;
#             font-size: 18px;
#             font-weight: bold;
#             padding: 10px;
#             background-color: #f8f9fa;
#             border-bottom: 2px solid #ddd;
#         }
#         .nav-bar a {
#             text-decoration: none;
#             color: black;
#         }
#         .nav-bar a:hover {
#             color: #007BFF;
#         }
#     </style>
#     <div class='nav-bar'>
#         <a href='/'>Home</a>
#         <a href='/projects'>Projects</a>
#         <a href='/about'>About Me</a>
#     </div>
#     <br>
# """, unsafe_allow_html=True)
#
# # Create Two Columns for Name/Photo & Professional Summary
# col1, col2 = st.columns([1.5, 2.5])
#
# with col1:
#     st.title("Avinash Pandey")
#     st.image("images/photo.jpg", width=250)  # Replace with actual file
#
# with col2:
#     st.subheader("Professional Summary")
#     st.markdown(
#         """
#         Highly motivated software and data engineer with experience in Machine Learning, AI, and Data Engineering.
#         Strong expertise in building end-to-end ML pipelines and software systems. Passionate about solving real-world
#         problems through technology.
#         """
#     )
#
# # Resume Section
# st.subheader("📄 Resume")
# st.markdown("Choose a version of my resume to download:")
# resume_col1, resume_col2, resume_col3 = st.columns(3)
# with resume_col1:
#     with open("images/Avinash Pandey Resume DS.pdf", "rb") as file:
#         st.download_button("📥 General Resume", file, file_name="Avinash_Pandey_Resume_General.pdf")
# with resume_col2:
#     with open("images/Avinash Pandey Resume ML.pdf", "rb") as file:
#         st.download_button("📥 Software Engineering Resume", file, file_name="Avinash_Pandey_Resume_SWE.pdf")
# with resume_col3:
#     with open("images/Avinash Pandey Resume SWE.pdf", "rb") as file:
#         st.download_button("📥 Data Science Resume", file, file_name="Avinash_Pandey_Resume_DS.pdf")
#
# # Contact Information
# st.subheader("📬 Contact & Professional Platforms")
# st.markdown("""
# - 📧 [Email](mailto:aopandey24@gmail.com)
# - 🔗 [LinkedIn](https://www.linkedin.com/in/avinashopandey/)
# - 🛠 [GitHub](https://github.com/Aopandey)
# """)
#
# # Skills Section
# st.subheader("🛠 Skills")
# st.markdown("""
# **Programming Languages:** Python, C++, Java
# **Frameworks:** TensorFlow, React, Flask
# **Tools:** Docker, Git, AWS
# """)
#
# # Work Experience Section with Hover Effect
# st.subheader("💼 Work Experience")
# st.markdown("""
# <style>
#     .work-item {
#         padding: 10px;
#         margin-bottom: 10px;
#         background-color: #1e1e1e;
#         color: white;
#         border-radius: 5px;
#         transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
#     }
#     .work-item:hover {
#         transform: translateY(-3px);
#         box-shadow: 0px 4px 8px rgba(255, 255, 255, 0.2);
#     }
# </style>
# <div class='work-item'>
#     <strong>Google | Software Engineer Intern</strong> (June 2023 - Dec 2023) <br>
#     - Developed a scalable ML pipeline that improved inference speeds by 30%
#     - Built REST APIs for AI-powered analytics dashboards
# </div>
# <div class='work-item'>
#     <strong>Purdue University | Research Assistant</strong> (Aug 2022 - May 2023) <br>
#     - Conducted research on AI-driven news classification models
#     - Published findings in IEEE AI Conference
# </div>
# """, unsafe_allow_html=True)
