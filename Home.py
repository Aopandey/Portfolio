import streamlit as zx
import pandas

zx.set_page_config(layout="wide")
col1, col2 = zx.columns(2)
row1 = zx.subheader(1)

with col1:
    zx.image("images/photo.jpg")

with col2:
    zx.title("Avinash Pandey")
    content = """
    I am a Senior majoring in Computer Science at the Purdue University Indianapolis.
    I am looking to further my knowledge and gain more experience in the Software Development and Cloud Computing field 
    through an internship in Summer. I have a strong passion for Programming, App development, Web development, problem-solving, and data analysis. 
    I am hard-working, focused, objective-oriented with proven knowledge of Python, JavaScript, C, C++, Java, HTML, CSS, and SQL.
    In addition, I also possess problem-solving and analytical skills and can speak multiple languages.
    """
    zx.info(content)

with row1:
    subhead = "Below you can find some of the apps I've built. Feel free to contact me!"

    zx.info(subhead)

col3, empty_col, col4 = zx.columns([1.5, 0.5, 1.5])

data = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in data[:10].iterrows():
        zx.header(row["title"])
        zx.write(row["description"])
        zx.write(f"[Source Code]({row['url']})")
        zx.image("images/" + row["image"])


with col4:
    for index, row in data[10:].iterrows():
        zx.header(row["title"])
        zx.write(row["description"])
        zx.write(f"[Source Code]({row['url']})")
        zx.image("images/" + row["image"])

