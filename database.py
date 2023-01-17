import pymysql
from application import DATABASE_PASSWORD


def mysql_CONNECTION():
	"""
    This function creates a connection to a MySQL database using the PyMySQL library.
    It returns the connection object.
    """
	connection=pymysql.connect(host='database-2.cniq3f7gind2.us-east-1.rds.amazonaws.com',port=3306,user='admin',password=DATABASE_PASSWORD,db='kaimedb',) 
	return connection



def insert_to_DATABASE(user,email,payday,percent,payPeriod,savings,payDate,reminderSent):
	 """
    This function inserts user data into the 'saversAccount' table in the MySQL database.
    :param user: str, the name of the user
    :param email: str, the email address of the user
    :param payday: str, the day of the month on which the user gets paid
    :param percent: str, the percent of the user's income that they want to save
    :param payPeriod: str, the pay period of the user (i.e. weekly, bi-weekly, monthly)
    :param savings: str, the user's calculated savings
    :param payDate: str, the user's next pay date
    :param reminderSent: str, a flag indicating whether a reminder has been sent to the user
    """
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

