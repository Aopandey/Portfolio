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
# with open("images/Avinash Pandey Resume ML.pdf", "rb") as pdf_file:
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
#         file_name="Avinash Pandey Resume ML.pdf",
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
# # Concepts Learning
# st.write("---")
# st.subheader("Concepts Learning")
# st.write("""
# - **Machine Learning Operations (MLOps):** Implementing and managing machine learning pipelines and workflows in production.
# - **Cloud Integration:** Learning Docker, Azure, and Dagster for scalable and efficient deployment of applications.
# - **Metadata Filtering Algorithms:** Improving precision in summarized research outputs.
# - **Automated Data Processing:** Using tools like ZenML and Prefect for efficient data handling.
# - **Streamlit Applications:** Developing user-friendly web applications for data visualization and interaction.
# - **Frontend Development with React:** Building dynamic and responsive web applications using React.js, including state management with Redux.
# - **API Integration:** Connecting frontend applications with backend services through RESTful APIs.
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
import pandas as pd
import base64
from PIL import Image

# Page Configuration
st.set_page_config(page_title="Portfolio | Avinash Pandey", layout="wide")

# Load CSS
with open("styles/main.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("Navigation")
sections = ["Home", "Projects", "Skills", "Resume", "Contact"]
selected_section = st.sidebar.radio("Go to", sections)

# Home Section
if selected_section == "Home":
    st.title("👋 Hi, I'm Avinash Pandey!")
    st.write("AI & Data Engineering Enthusiast | Machine Learning Engineer | Software Developer")

    # Profile Picture
    col1, col2 = st.columns([3, 1])
    with col2:
        profile_pic = Image.open("images/photo.jpg")
        st.image(profile_pic)

    # Quick Links
    st.markdown("---")
    st.subheader("Professional Platforms")
    social_media = {
        "LinkedIn": "https://www.linkedin.com/in/avinashopandey/",
        "GitHub": "https://github.com/Aopandey"
    }
    cols = st.columns(len(social_media))
    for index, (platform, link) in enumerate(social_media.items()):
        cols[index].markdown(f"[💻 {platform}]({link})")

# Projects Section
elif selected_section == "Projects":
    st.subheader("💡 Featured Projects")
    data = pd.read_csv("data.csv", sep=";")

    for _, row in data.iterrows():
        with st.container():
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image("images/" + row["image"], use_column_width=True)
            with col2:
                st.subheader(row["title"])
                st.write(row["description"])
                st.markdown(f"[🔗 View Source Code]({row['url']})")
            st.markdown("---")

# Skills Section
elif selected_section == "Skills":
    st.subheader("🛠 Skills & Technologies")
    skills = {
        "Python": "🐍", "C++": "🟦", "SQL": "💾", "TensorFlow": "🔶", "Docker": "🐳", "AWS": "☁️", "React.js": "⚛️"
    }
    cols = st.columns(len(skills))
    for index, (skill, emoji) in enumerate(skills.items()):
        cols[index].markdown(f"<p style='text-align:center; font-size: 20px'>{emoji} {skill}</p>",
                             unsafe_allow_html=True)

# Resume Section
elif selected_section == "Resume":
    st.subheader("📄 Download My Resume")
    resume_options = {
        "Software Engineer Resume": "Avinash Pandey Resume SWE.pdf",
        "Machine Learning Resume": "Avinash Pandey Resume DS.pdf",
        "Data Engineer Resume": "Avinash Pandey Resume DE.pdf"
    }
    selected_resume = st.selectbox("Choose Resume:", list(resume_options.keys()))
    with open(f"resumes/{resume_options[selected_resume]}", "rb") as pdf_file:
        st.download_button(
            label="📁 Download Selected Resume",
            data=pdf_file.read(),
            file_name=resume_options[selected_resume],
            mime="application/octet-stream",
        )

# Contact Section
elif selected_section == "Contact":
    st.subheader("📬 Contact Me")
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Your Message")
        submit = st.form_submit_button("Send Message ✉️")
        if submit:
            st.toast("✅ Your message has been sent!")

