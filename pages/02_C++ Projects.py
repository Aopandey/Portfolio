import streamlit as zx
import pandas

with open("styles/main.css") as f:
    zx.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

image_width = 300
row4 = zx.subheader(1)

with row4:
    subhead3 = "Projects with C++"
    zx.header(subhead3)

col7, empty_col, col8 = zx.columns([1.5, 0.5, 1.5])

data = pandas.read_csv("data.csv", sep=";")

with col7:
    for index, row in data[8:10].iterrows():
        zx.subheader(row["title"])
        zx.write("---")
        zx.write(row["description"])
        zx.write(f"[🌟Source Code]({row['url']})")
        zx.image("images/" + row["image"], width=image_width)

with col8:
    for index, row in data[10:11].iterrows():
        zx.subheader(row["title"])
        zx.write("---")
        zx.write(row["description"])
        zx.write(f"[🌟Source Code]({row['url']})")
        zx.image("images/" + row["image"],  width=image_width)