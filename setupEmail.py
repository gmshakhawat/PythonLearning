import smtplib

host="smtp.gamil.com"
port=587
username="shakhawatislam96@gmail.com"
password="reeere"
from_email=username
to_list=["shakhawatislam96@gmail.com"]

email_conn=smtplib.SMTP(host, port)
email_conn.ehlo()
email_conn.sendmail(from_email,"hello there am here for testing your id ")
email_conn.quit()
