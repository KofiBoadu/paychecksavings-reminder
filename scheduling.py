import sqlite3
import sched 
import time
import datetime
from email.message import EmailMessage
from email.utils import formataddr
import smtplib
from database import *
import pymysql



def sending_emailReminders(recieverEmail,name,amount2Save):
	senderEmail= "kboadu16@gmail.com"
	msg = EmailMessage()
	msg["Subject"] = "Paycheck Savings Reminder"
	msg["From"] = formataddr(("KAIME.CORP", f"{senderEmail}"))
	msg["To"] = recieverEmail
	msg["BCC"] = senderEmail
	msg.set_content(
                        f"""\
                              Hi {name},
                              I hope you are well.
                               Please remember to  save  <strong style="color:green;">USD{amount2Save}</strong> Today .
                              KAIME LLC
                              """
                    )
	msg.add_alternative(
              f"""\
          <html>
            <body>
              <p>Hi {name},</p>
              <p>I hope you are well.</p>
              <p> Please remember to  save <strong style="color:green;">{amount2Save}USD</strong> Today </p>
              <p>Best regards</p>
              <strong style="color: red ;">KAIME</strong>
            </body>
          </html>
          """,
              subtype="html",
          )
	with smtplib.SMTP('smtp.gmail.com',587) as server:
		server.starttls()
		server.login("kboadu16@gmail.com", "xoaryqsilwhrsseh")
		server.sendmail(senderEmail,recieverEmail,msg.as_string())


def database_queryResults():
	weekday=datetime.datetime.now().date().weekday()
	weekdays= {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
	day=weekdays[weekday]
	date=str(datetime.datetime.now().date())
	with pymysql.connect(host='database-2.cniq3f7gind2.us-east-1.rds.amazonaws.com',port=3306,user='admin',password='kaime2023',db='kaimedb',) as connection:
		c= connection.cursor()
		c.execute("SELECT * FROM saversAccount WHERE payDay=%s AND payDate=%s AND reminderSent='False' ",(day,date,))
		data= c.fetchall()
		return data 


def update_database():
	weekday=datetime.datetime.now().date().weekday()
	weekdays= {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
	day=weekdays[weekday]
	date=str(datetime.datetime.now().date())
	with pymysql.connect(host='database-2.cniq3f7gind2.us-east-1.rds.amazonaws.com',port=3306,user='admin',password='kaime2023',db='kaimedb',) as connection:
		c= connection.cursor()
		c.execute("UPDATE saversAccount SET reminderSent = 'True' WHERE reminderSent='False' AND payDay=%s AND payDate=%s",(day,date,))
		connection.commit()



def  schedule_reminders():
	s = sched.scheduler(time.time, time.sleep)
	users_toRemind= database_queryResults()
	for user_data in users_toRemind:
		sending_emailReminders(user_data[1],user_data[0],user_data[5]) 



def reminder_run():
	while True:
		s = sched.scheduler(time.time, time.sleep)
		s.enter(1,1,schedule_reminders)
		s.run()
		if s.empty():
			update_database()
		time.sleep(60)



if __name__=="__main__":
	reminder_run()
	
	

