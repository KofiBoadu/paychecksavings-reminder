import sched 
import time
import datetime
from email.message import EmailMessage
from email.utils import formataddr
import smtplib
import pymysql
from reminder import * 
from database import *



def sending_emailReminders(recieverEmail,name,amount2Save):
	senderEmail= "kboadu16@gmail.com"
	msg = EmailMessage()
	msg["Subject"] = "Paycheck Savings Reminder"
	msg["From"] = formataddr(("KAIME ", f"{senderEmail}"))
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

	"""
	This function queries a MySQL database for rows in the 'saversAccount' 
	table where payDay is the current day, payDate is today, 
	and reminderSent is false. The function returns all the data fetched by the query.

	"""

	today=datetime.date.today()
	current_day_of_week = today.isoweekday()
	weekdays= {1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}
	day=weekdays[current_day_of_week]
	date= today
	connection= mysql_CONNECTION()
	c= connection.cursor()
	c.execute("SELECT * FROM saversAccount WHERE payDay=%s AND payDate=%s AND reminderSent='False' ",(day,date,))
	data= c.fetchall()
	return data 




def update_database():
	"""
	This function updates the 'reminderSent' field in the 'saversAccount' table for all rows where reminderSent=False, 
	payDay is the current day and payDate is today in a MySQL database by setting the 'reminderSent' field to 'True'.

	This will help avoid sending multiple reminders becuase , the reminders are only sent when the 
	reminderSent= False

	"""
	weekday=datetime.datetime.now().date().weekday()
	weekdays= {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
	day=weekdays[weekday]
	date=str(datetime.datetime.now().date())
	connection= mysql_CONNECTION()
	c= connection.cursor()
	c.execute("UPDATE saversAccount SET reminderSent = 'True' WHERE reminderSent='False' AND payDay=%s AND payDate=%s",(day,date,))
	connection.commit()



def  schedule_reminders():
	"""
	This function retrieves all rows from 'saversAccount' table in the database where payDay is the current day, payDate is today, and reminderSent is false, and sends an email reminder to each user using the sending_emailReminders() function. 
	The function uses a scheduler to schedule the sending of email reminders.
	"""
	s = sched.scheduler(time.time, time.sleep)
	users_toRemind= database_queryResults()
	for user_data in users_toRemind:
		sending_emailReminders(user_data[1],user_data[0],user_data[5]) 



def reminder_run():
	"""
	This function uses the scheduler to run the schedule_reminders() function after 1 second delay and then check if the scheduler is empty,
	 if so it will update the database using update_database() function.
	 """
	s = sched.scheduler(time.time, time.sleep)
	s.enter(1,1,schedule_reminders)
	s.run()
	if s.empty():
		update_database()




	
	

