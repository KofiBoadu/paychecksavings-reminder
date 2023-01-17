import pymysql


def mysql_CONNECTION():
	connection=pymysql.connect(host='database-2.cniq3f7gind2.us-east-1.rds.amazonaws.com',port=3306,user='admin',password='kaime2023',db='kaimedb',) 
	return connection



def insert_to_DATABASE(user,email,payday,percent,payPeriod,savings,payDate,reminderSent):
	connection=mysql_CONNECTION()
	cur=connection.cursor()
	values=[(user,email,payday,percent,payPeriod,savings,payDate,reminderSent),]
	stmt="INSERT INTO saversAccount VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
	cur.executemany(stmt,values)
	connection.commit()



# connection=mysql_CONNECTION()
# cur=connection.cursor()
# cur.execute("DELETE FROM saversAccount WHERE Name='Daniel' ")
# connection.commit()
# # cur.execute("CREATE TABLE saversAccount(Name TEXT,Email TEXT,payDay TEXT,percent INT,payPeriod TEXT,savingsAmount INT ,payDate TEXT,reminderSent TEXT)")

