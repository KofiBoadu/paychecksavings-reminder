from flask import Flask, render_template,request, url_for,g,redirect, flash,session
import pymysql
import datetime
import os
from database import *
from reminder import *
from dotenv import load_dotenv

load_dotenv()

#ENVIRONMENT VARIABLES
EMAIL= os.getenv("EMAIL")
DATABASE_PASSWORD=os.getenv("DATABASE_PASSWORD")
EMAIL_PASSWORD=os.getenv("EMAIL_PASSWORD")
DATABASE_HOST= os.getenv("DATABASE_HOST")
SECRET_KEY= os.urandom(30)


application= Flask(__name__)
application.config.from_object(__name__)



@application.route('/',methods=['GET','POST'])
def add_to_database():
	"""
    This function is used for handling GET and POST requests for the 'add_to_database' route.
    If the request method is 'GET', it sets the 'log_on' session variable to True and renders the 'index.html' template.
    If the request method is 'POST', it retrieves user input from the request form, calculates the user's savings, 
    creates an instance of the 'EmailReminders' class, insert the user's details to the database, and redirects to the 'add_to_database' route.
    """
	if request.method== "GET":
		session['log_on']= True
		return render_template("index.html")

	if request.method=="POST":
		session.pop('log_on',None)
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
		insert_to_DATABASE(user,email,payday,percent,payPeriod,savings,payDate,reminderSent)
		USERFULLDETAILS.checkTodayDate()
		return redirect(url_for('add_to_database'))







	


	

	 

	

	


