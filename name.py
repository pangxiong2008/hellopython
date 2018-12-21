from email.mime.text import MIMEText
msg=MIMEText('hello','plain','utf-8')
from_address=input('From: ')
password=input('password: ')
to_addr=input('To: ')
smtp_server=input('SMTP server: ')
import smtplib
server=smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_address,password)
server.sendmail(from_address,[to_addr],msg.as_string())
server.quit()
