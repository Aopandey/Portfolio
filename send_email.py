import smtplib, ssl
import os


def send_mail(subject, body):
    host = "smtp.gmail.com"
    port = 465

    username = "avkr258@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "avkr258@gmail.com"
    context = ssl.create_default_context()

    message = f"Subject: {subject}\n\n{body}"

    try:
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
        # Depending on your application, you might want to handle the error differently,
        # such as logging the error or sending a notification to the administrator.

