import smtplib, ssl
import os



def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "jorgemail.affonso@gmail.com"
    #password = "..."
    password = os.getenv("PASSWORD")   # password for gmail application - saved in user environment variable
    receiver = "jorgemail.affonso@gmail.com"
    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

