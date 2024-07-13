import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

msg = MIMEMultipart()
msg["From"] = "annika.liang@gmail.com"
msg["To"] = "annica.liang@gmail.com
header = Header("Test Send Email","utf-8")"
msg["Subject"] = header.encode()

body = "This is the email sent from python"
msg.attach(MIMEText(body))
#mbody = MIMEText(body)
#msg.attach(mbody)
ssl_context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=ssl_context) as server:
    server.login("annika.liang@gmail.com","txni jseq fcrr mpsx")
    server.sendmail("annika.liang@gmail.com","annica.liang@gmail.com",msg.as_string())
print("Sending the Email Successfully")
