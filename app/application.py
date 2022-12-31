from reminder import *
from flask import Flask, render_template,request, url_for,g,redirect, flash,session
import sqlite3
import datetime
import os



#configurations
DATABASE= 'save.db'
SECRET_KEY= os.urandom(30)


application= Flask(__name__)
application.config.from_object(__name__)


#connecting to database
def connect_db():
	return sqlite3.connect(application.config['DATABASE'])

#My route to get user details and append to the database 

@application.route('/',methods=['GET','POST'])

def add_to_database():
	if request.method== "GET":
		session['log_on']= True
		return render_template("index.html")

	if request.method=="POST":
		session.pop('log_on',None)
		g.db= connect_db()
		percent= request.form['percent']
		hourWage= request.form['hourWage']
		USERINCOME= UserIncomeCalculator(percent,hourWage)
		savings= USERINCOME.weekSavings()
		user= request.form['username']
		email=request.form['email']
		payday=request.form['payday'].capitalize()
		payPeriod= request.form['payperiod']
		reminderSent= "False"
		USERFULLDETAILS= EmailReminders(payday, user, email,USERINCOME.percentageToSave,USERINCOME.hourWage)
		USERFULLDETAILS.set_payPeriod(payPeriod)
		payDate= USERFULLDETAILS.next_PayDate()
		values=[(user,email,payday,percent,payPeriod,savings,payDate,reminderSent)]
		g.db.executemany("INSERT INTO saversAccount VALUES (?,?,?,?,?,?,?,?)",values)
		g.db.commit()
		g.db.close()
		data= USERFULLDETAILS.checkTodayDate()
		return redirect(url_for('add_to_database'))








# if __name__=="__main__":
# 	app.run(debug=True)
	



	 

	

	


