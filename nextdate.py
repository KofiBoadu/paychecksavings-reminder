import datetime
import time 
from reminder import *
import pymysql
from database import * 



def return_next_date(payday, payperiod):
	user= EmailReminders(payday)
	user.set_payPeriod(payperiod)
	return user.next_PayDate()


def setNew_schedule_DATE():
	weekday=datetime.datetime.now().date().weekday()
	weekdays= {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
	day=weekdays[weekday]
	print(day)
	date=str(datetime.datetime.now().date())
	print(date)
	connection= mysql_CONNECTION()
	# with pymysql.connect(host='database-2.cniq3f7gind2.us-east-1.rds.amazonaws.com',port=3306,user='admin',password='kaime2023',db='kaimedb',) as connection:
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




		
# def setNew_schedule_DATE():
#     weekday = datetime.datetime.now().date().weekday()
#     weekdays = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
#     day = weekdays[weekday]
#     date = str(datetime.datetime.now().date())

#     new_dates = []

#     with pymysql.connect(host='database-2.cniq3f7gind2.us-east-1.rds.amazonaws.com', port=3306, user='admin', password='kaime2023', db='kaimedb') as connection:
#         c = connection.cursor()

#         try:
#             c.execute("SELECT email, payDay, payPeriod FROM saversAccount WHERE payDay != %s AND payDate != %s", (day, date))
#             rows = c.fetchall()

#             for row in rows:
#                 new_date = return_next_date(row[1], row[2])
#                 new_dates.append((row[0], new_date))

#             c.executemany("UPDATE saversAccount SET payDate = %s, reminderSent = 'True' WHERE Email = %s", new_dates)
#             connection.commit()
#         except Exception as e:
#             print(e)











if __name__=="__main__":
	setNew_schedule_DATE()
	




			



			
	