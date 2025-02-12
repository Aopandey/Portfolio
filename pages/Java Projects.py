import streamlit as zx
import pandas

with open("styles/main.css") as f:
    zx.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

image_width = 300
row3 = zx.subheader(1)

with row3:
    subhead2 = "Projects with Java"
    zx.header(subhead2)

col5, empty_col, col6 = zx.columns([1.5, 0.5, 1.5])

data = pandas.read_csv("data.csv", sep=";")

with col5:
    for index, row in data[6:7].iterrows():
        zx.subheader(row["title"])
        zx.write("---")
        zx.write(row["description"])
        zx.write(f"[🌟Source Code]({row['url']})")
        zx.image("images/" + row["image"], width=image_width)

with col6:
    for index, row in data[7:8].iterrows():
        zx.subheader(row["title"])
        zx.write("---")
        zx.write(row["description"])
        zx.write(f"[🌟Source Code]({row['url']})")
        zx.image("images/" + row["image"], width=image_width)
