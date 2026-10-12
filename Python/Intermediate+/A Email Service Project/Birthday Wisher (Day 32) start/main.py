import smtplib
import datetime
import random
current=datetime.datetime.now()
with open("quotes.txt","r") as file:
    quotes=file.readlines()
if current.weekday()==0:
    with smtplib.SMTP("smtp.gmail.com",587) as conn:
        conn.starttls()
        conn.login(user="spaadi1601@gmail.com",password="cpty soiw wyhq qtwo")
        conn.sendmail(from_addr="spaadi1601@gmail.com",to_addrs="aadisp16@yahoo.com",msg=f"Subject: Monday Motivational Quotes\n\n{random.choice(quotes)}")
