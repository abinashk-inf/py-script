import smtplib
from email.mime.text import MIMEText

source=''  #your email
password=''#your email password
body="This is a test mail"
msg=MIMEText(body);
msg['Subject']='Test mail'
msg['To']=''#destination email
msg['From']=source

server=smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.startls()
server.login(source,password)
server.send_message()
