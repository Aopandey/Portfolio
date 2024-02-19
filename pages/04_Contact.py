import streamlit as zx
from send_email import send_mail

with open("styles/main.css") as f:
    zx.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

zx.header("Contact Me!")

with zx.form(key="email_page"):
    user = zx.text_input("Your Email Address")
    text = zx.text_area("Your Message")
    subject = f"New Email from {user}"
    body = f"From: {user}\n{text}"

    button = zx.form_submit_button("Submit")

    if button:
        send_mail(subject, body)
        zx.info("Email Sent!")
