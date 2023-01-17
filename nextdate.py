import datetime
import time 
from reminder import *
import pymysql
from database import * 



def return_next_date(payday, payperiod):
	"""
	return_next_date(payday, payperiod) - Returns the next pay date for a user based on the input payday and payperiod.

	Inputs:
	payday (str) - the current payday in the format 'YYYY-MM-DD'
	payperiod (str) - the pay period (e.g. 'bi-weekly', 'monthly')

	Returns:
	next_paydate (str) - the next pay date in the format 'YYYY-MM-DD'
	"""
	user= EmailReminders(payday)
	user.set_payPeriod(payperiod)
	return user.next_PayDate()




def setNew_schedule_DATE():
	"""
	This function sets new schedule dates for saversAccount in a MySQL database. 
    It first retrieves the current weekday and date, 
    then selects email, payDay, and payPeriod for all accounts where payDay and payDate do not match the current values.
     It then calculates the next payDate for each account using the return_next_date() function and updates the payDate and
      reminderSent fields in the database for each account. The new_dates dictionary is then cleared."

	"""
	weekday=datetime.datetime.now().date().weekday()
	weekdays= {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
	day=weekdays[weekday]
	date=str(datetime.datetime.now().date())
	connection= mysql_CONNECTION()
	c= connection.cursor()
	c.execute("SELECT email,payDay, payPeriod FROM saversAccount WHERE  payDay !=%s AND payDate !=%s  ",(day,date,))
	new_dates={}
	for row in c:
		new_dates[row[0]]=return_next_date(row[1],row[2])
	for key, value in new_dates.items():
		c.execute("UPDATE saversAccount SET payDate=%s  WHERE  Email=%s ",(value,key,))
		c.execute("UPDATE saversAccount SET reminderSent=%s  WHERE  Email=%s ",('False',key,))
		connection.commit()
	new_dates.clear()












			



			
	