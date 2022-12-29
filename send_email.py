import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "jorgemail.affonso@gmail.com"
    password = "ffdmwzibpnvrzuph"
    receiver = "jorgemail.affonso@gmail.com"
    my_context = ssl.create_default_context()
#    message = """\
#Subject: Hi!
#How are you doing ?
#Bye!
#"""
    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

