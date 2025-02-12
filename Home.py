# import streamlit as st
# import pandas as pd
# import base64
# from pathlib import Path
# from PIL import Image

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
description1 = ("""\
<span style="font-size:1.2em;">
I am passionate about leveraging <span style="color:#1E90FF; font-weight:bold;">AI, Machine Learning, and Data Engineering</span> to develop scalable data pipelines, optimize AI-driven workflows, and extract <span style="color:#FF6347; font-weight:bold;">actionable insights</span> from complex datasets.
<br><br>
I graduated from <span style="color:#1E90FF; font-weight:bold;">Purdue University</span> with a <span style="color:#1E90FF; font-weight:bold;">B.S. in Computer Science</span> and a <span style="color:#1E90FF; font-weight:bold;">Minor in Mathematics</span>.
<br><br>
My most recent experience at <span style="color:#1E90FF; font-weight:bold;">Aider Ventures</span> involved engineering an automated ETL pipeline that processed <span style="color:#FF6347; font-weight:bold;">10,000+ research papers</span> from <span style="color:#1E90FF; font-weight:bold;">ICML 2024</span>, integrating <span style="color:#FF6347; font-weight:bold;">FAISS embeddings, ChromaDB, and LangChain</span> to improve retrieval accuracy and metadata extraction by <span style="color:#FF6347; font-weight:bold;">20%</span>. This transformed unstructured research text into structured data, enhancing data retrieval and downstream analysis. I also built interactive visualizations to analyze AI research trends, providing structured insights for non-technical stakeholders.
<br><br>
My expertise spans <span style="color:#FF6347; font-weight:bold;">Python, SQL, AWS, Docker</span>, <span style="color:#FF6347; font-weight:bold;">Machine Learning (Scikit-learn, PyTorch, TensorFlow)</span>, and <span style="color:#FF6347; font-weight:bold;">Data Visualization (Tableau, Power BI, Matplotlib)</span>. I excel at bridging AI, data engineering, and business strategy, transforming complex data into impactful solutions.
</span>
""")
social_media = {
    "Email": {
         "link": "mailto:aopandey24@gmail.com",
         "icon": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png"
    },
    "LinkedIn": {
         "link": "https://www.linkedin.com/in/avinashopandey/",
         "icon": "https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png"
    },
    "GitHub": {
         "link": "https://github.com/Aopandey",
         "icon": "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"
    }
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
    st.markdown("<div style='margin-left: 100px;'><h1 style='text-align: center;'>{}</h1></div>".format(name),
                unsafe_allow_html=True)
    spacer, image_col = st.columns([1, 7])
    with image_col:
        st.image(profile_pic, width=500)
with col_right:
    st.markdown("<div style='margin-left: 100px; margin-right: 400px; margin-top: 80px;'>{}</div>".format(description1), unsafe_allow_html=True)

st.markdown("<br><br><br>", unsafe_allow_html=True)

# --- NARROW CONTENT AREA (Using Columns) ---
# Create three columns: left spacer, center content, and right spacer.
left_spacer, content_col, right_spacer = st.columns([1, 3, 1])

with content_col:
    # RESUME SECTION
    st.write("---")
    st.subheader("Resume")
    st.markdown("<br>", unsafe_allow_html=True)
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
    st.markdown("<br>", unsafe_allow_html=True)
    platform_cols = st.columns(len(social_media))
    for idx, (platform, details) in enumerate(social_media.items()):
        # Build the markdown string with an image and a link.
        # The target='_blank' makes the link open in a new tab.
        md = (
            f"<a href='{details['link']}' target='_blank'>"
            f"<img src='{details['icon']}' width='30' style='vertical-align: middle; margin-right: 10px;'>"
            f"{platform}</a>"
        )
        platform_cols[idx].markdown(md, unsafe_allow_html=True)

    # TECHNICAL SKILLS SECTION
    st.write("---")
    st.subheader("Technical Skills")
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <span style='color:#1E90FF; font-size:1.3em; font-weight:bold;'>Programming Languages & Development</span>  
    - <span style='color:#FF6347; font-weight:bold;'>Languages:</span> Python, Java, C++, JavaScript, TypeScript, R  
    - <span style='color:#FF6347; font-weight:bold;'>Frameworks & Libraries:</span> Flask, FastAPI, Django, Node.js, ReactJS  

    <span style='color:#1E90FF; font-size:1.3em; font-weight:bold;'>Data Science & AI Development</span>  
    - <span style='color:#FF6347; font-weight:bold;'>Machine Learning:</span> Scikit-learn, XGBoost, PyTorch, TensorFlow, Spark MLlib  
    - <span style='color:#FF6347; font-weight:bold;'>Deep Learning:</span> Multi-Model Learning, Transfer Learning, Representation Learning, NLP (Text Classification, Sentiment Analysis, Named Entity Recognition, Topic Modeling)  
    - <span style='color:#FF6347; font-weight:bold;'>AI Applications:</span> Predictive Analytics, Time Series Forecasting, Anomaly Detection, Customer Segmentation  

    <span style='color:#1E90FF; font-size:1.3em; font-weight:bold;'>Big Data, Cloud & ETL</span>  
    - <span style='color:#FF6347; font-weight:bold;'>Databases:</span> MySQL, MongoDB, DynamoDB, SQL Server  
    - <span style='color:#FF6347; font-weight:bold;'>Cloud & DevOps:</span> AWS (EC2, S3, Lambda), Docker, Kubernetes  
    - <span style='color:#FF6347; font-weight:bold;'>Data Engineering:</span> FAISS, ChromaDB, Data Warehousing, ETL Pipelines, Data Orchestration, Streaming Data Processing, Dagster  

    <span style='color:#1E90FF; font-size:1.3em; font-weight:bold;'>Software Engineering & System Design</span>  
    - <span style='color:#FF6347; font-weight:bold;'>Development Tools:</span> RESTful APIs, GraphQL, Git, GitHub Actions, Jenkins, CI/CD Pipelines  
    - <span style='color:#FF6347; font-weight:bold;'>System Design:</span> Scalability, Microservices, Load Balancing, Caching Strategies, API Optimization, Performance Tuning  

    <span style='color:#1E90FF; font-size:1.3em; font-weight:bold;'>Data Visualization & Business Intelligence</span>  
    - <span style='color:#FF6347; font-weight:bold;'>Visualization Tools:</span> Tableau, Power BI, Matplotlib, Seaborn  
    """, unsafe_allow_html=True)

    # WORK EXPERIENCE SECTION
    st.write("---")
    st.subheader("Work Experience")
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    **<span style='color:#1E90FF; font-size:1.3em; font-weight:bold;'>Aider Ventures (Nienna Lab)</span>** | **<span style='color:#1E90FF; font-size:1.3em; font-weight:bold;'>Machine Learning Engineering Intern</span>** (<span style='color:#1E90FF; font-weight:bold;'>July 2024 – Nov 2024</span>)
    - Developed and optimized an automated ETL pipeline that processed **<span style='color:#FF6347; font-weight:bold;'>10,000+ research papers</span>** from **<span style='color:#1E90FF; font-weight:bold;'>ICML 2024</span>**, leveraging **<span style='color:#FF6347; font-weight:bold;'>FAISS embeddings, ChromaDB, and LangChain</span>** to convert unstructured research text into structured data, improving retrieval accuracy and metadata extraction by **<span style='color:#FF6347; font-weight:bold;'>20%</span>**.
    - Engineered scalable classification models using the **<span style='color:#FF6347; font-weight:bold;'>Gemini API</span>**, improving content organization and research trend analysis by **<span style='color:#FF6347; font-weight:bold;'>40%</span>**, enabling better semantic search and categorization of research insights.
    - Implemented metadata filtering algorithms in **<span style='color:#FF6347; font-weight:bold;'>LangChain</span>**, refining data enrichment processes and enhancing the precision of extracted insights by **<span style='color:#FF6347; font-weight:bold;'>20%</span>** to improve downstream AI applications.
    - Built an interactive data visualization framework to analyze AI research trends, presenting insights on top universities, research areas, and general topic distributions to help non-technical stakeholders identify startup and collaboration opportunities.
    - Integrated AI-powered retrieval techniques to streamline query-based document access, reducing information retrieval time for users in business and research settings.
    - Optimized data processing pipelines using containerization (**<span style='color:#FF6347; font-weight:bold;'>Docker, Kubernetes</span>**), ensuring scalability and efficient deployment of AI-driven solutions.

    <br><br>

    **<span style='color:#1E90FF; font-size:1.3em; font-weight:bold;'>Legislative Services Agency</span>** | **<span style='color:#1E90FF; font-size:1.3em; font-weight:bold;'>Business Analyst Intern</span>** (<span style='color:#1E90FF; font-weight:bold;'>Dec 2023 – Mar 2024</span>)
    - Designed and managed SQL-based ETL workflows, achieving **<span style='color:#FF6347; font-weight:bold;'>98% data accuracy</span>** in validating and preprocessing Indiana General Assembly datasets.
    - Developed and optimized <span style='color:#FF6347; font-weight:bold;'>SQL queries</span> to enhance data extraction, transformation, and loading (ETL) efficiency for legislative reports and bill tracking.
    - Built <span style='color:#FF6347; font-weight:bold;'>Power BI and Tableau dashboards</span>, enabling real-time business intelligence reporting and improving legislative data analysis for decision-makers.
    - Automated data validation and reporting pipelines, significantly reducing manual data processing workloads and improving reporting efficiency.
    - Provided technical support and troubleshooting for legislative data systems, ensuring seamless integration of business intelligence tools for data-driven policy analysis.
    """, unsafe_allow_html=True)

