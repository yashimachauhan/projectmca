import smtplib
from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText

def emailsend(otp,email):
    fromadd = "Get Fit Advisor"
    toaddr = email
    msg = MIMEMultipart()
    msg['From']="manilmhjn7@gmail.com"
    msg['To']=email
    msg['Subject']="Otp"
    body="Your OTP is: "+str(otp)
    msg.attach(MIMEText(body,"plain"))
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login("kshivam1710@gmail.com","&shivam&1710@")
    text=msg.as_string()
    server.sendmail("kshivam1710@gmail.com","yashima92@gmail.com",text)
    server.quit()

emailsend("123",'kshivam1710@gmail.com')
