import pymysql

conn= pymysql.connect(host='database-2.cniq3f7gind2.us-east-1.rds.amazonaws.com',port=3306,user='admin',password='kaime2023',db='kaimedb',)


def insert_to_DATABASE(user,email,payday,percent,payPeriod,savings,payDate,reminderSent):
	cur=conn.cursor()
	values=[(user,email,payday,percent,payPeriod,savings,payDate,reminderSent),]
	stmt="INSERT INTO saversAccount VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
	cur.executemany(stmt,values)
	conn.commit()

# cur=conn.cursor()
# cur.execute("DROP TABLE IF EXISTS saversAccount")
# cur.execute("CREATE TABLE saversAccount(Name TEXT,Email TEXT,payDay TEXT,percent INT,payPeriod TEXT,savingsAmount INT ,payDate TEXT,reminderSent TEXT)")

