import streamlit as zx
import pandas

with open("styles/main.css") as f:
    zx.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

image_width = 300
row2 = zx.subheader(1)

with row2:
    subhead1 = "Projects with Python"
    zx.header(subhead1)

col3, empty_col, col4 = zx.columns([1.5, 0.5, 1.5])

data = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in data[:3].iterrows():
        zx.subheader(row["title"])
        zx.write("---")
        zx.write(row["description"])
        zx.write(f"[🌟Source Code]({row['url']})")
        zx.image("images/" + row["image"], width=image_width)


with col4:
    for index, row in data[3:6].iterrows():
        zx.subheader(row["title"])
        zx.write("---")
        zx.write(row["description"])
        zx.write(f"[🌟Source Code]({row['url']})")
        zx.image("images/" + row["image"], width=image_width)