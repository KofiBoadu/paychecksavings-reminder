import sqlite3
import datetime
import time 
from reminder import *
from database import *



def return_next_date(payday, payperiod):
	user= EmailReminders(payday)
	user.set_payPeriod(payperiod)
	return user.next_PayDate()


def setNew_schedule_DATE():
	weekday=datetime.datetime.now().date().weekday()
	weekdays= {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
	day=weekdays[weekday]
	date=str(datetime.datetime.now().date())
	with pymysql.connect(host='database-2.cniq3f7gind2.us-east-1.rds.amazonaws.com',port=3306,user='admin',password='kaime2023',db='kaimedb',) as connection:
		c= connection.cursor()
		c.execute("SELECT email,payDay, payPeriod FROM saversAccount WHERE  payDay !=%s AND payDate !=%s  ",(day,date,))
		new_dates={}
		for row in c:
			new_dates[row[0]]=return_next_date(row[1],row[2])
		for key, value in new_dates.items():
			c.execute("UPDATE saversAccount SET payDate=%s  WHERE  Email=%s ",(value,key,))
			c.execute("UPDATE saversAccount SET reminderSent=%s  WHERE  Email=%s ",('False',key,))
		new_dates.clear()

		


def reminder_run():
	while True:
		setNew_schedule_DATE()
		time.sleep(86400)




if __name__=="__main__":
	reminder_run()

	


			



			
	