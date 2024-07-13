import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = "annika.liang@gmail.com"
receiver = ["annica.liang@gmail.com","annika.liang@gmail.com"]
for I in receiver:
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = I
    header = Header("Test Send Email","utf-8")
    msg["Subject"] = header.encode()

    body = "This is the email sent from python."
    msg.attach(MIMEText(body))
    #mbody = MIMEText(body)
    #msg.attach(mbody)
    ssl_context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=ssl_context) as server:
        server.login(sender,"txni jseq fcrr mpsx")
        server.sendmail(sender,I,msg.as_string())
    print("Sending the Email Successfully")
