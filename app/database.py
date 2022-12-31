import sqlite3, datetime

with sqlite3.connect("save.db") as connection:
	c= connection.cursor()
	c.execute("DROP TABLE IF EXISTS saversAccount")
	c.execute("CREATE TABLE saversAccount(Name,Email,payDay,percent,payPeriod,savingsAmount,payDate,reminderSent)")
	