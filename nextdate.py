import sqlite3
import datetime
import time 
from reminder import *



def return_next_date(payday, payperiod):
	user= EmailReminders(payday)
	user.set_payPeriod(payperiod)
	return user.next_PayDate()


def database_queryResults():
	weekday=datetime.datetime.now().date().weekday()
	weekdays= {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
	day=weekdays[weekday]
	date=str(datetime.datetime.now().date())
	with sqlite3.connect('save.db') as connection:
		c= connection.cursor()
		c.execute("SELECT email,payDay, payPeriod FROM saversAccount WHERE  payDay !=? AND payDate !=?  ",(day,date,))
		new_dates={}
		for row in c:
			new_dates[row[0]]=return_next_date(row[1],row[2])
		for key, value in new_dates.items():
			c.execute("UPDATE saversAccount SET payDate=?  WHERE  Email=? ",(value,key,))
			c.execute("UPDATE saversAccount SET reminderSent=?  WHERE  Email=? ",('False',key,))
		new_dates.clear()

		


def reminder_run():
	while True:
		database_queryResults()
		time.sleep(1200)




if __name__=="__main__":
	reminder_run()

	


			



			
	