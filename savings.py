import datetime

import calendar

import smtplib


import datetime
import calendar
import smtplib



class Signup:
    
    def __init__(self,full_name,email):
        
        self.full_name=full_name
        self.email=email
        
    def __str__(self):
        
        return f"hey {self.full_name} welcome"
    
        
class Savings:
    
    def __init__(self,percentage,hour_wage,week_hours):
        
        self.percentage=percentage
        self.hour_wage=hour_wage
        self.week_hours=week_hours
        
    def weekly(self):
        
        return self.hour_wage * self.week_hours
    
    def monthly(self):
        
        return Savings.weekly(self)*4
    
    def annually(self):
        
        return Savings.monthly(self)*12
    
    def final_savings(self):
        
        return f"USD{self.percentage/100*Savings.weekly(self)}" 
    
    
    
def paycheck():
    
    days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    
    return days


"""
This is testing of the entire script
////////////////
"""

if __name__== '__main__':
    
    create_account= Signup(input("full name: "),input("email: "))
    print(f"Hey {create_account.full_name} fill out the forms below and start SAVING!")
    start= Savings(int(input("what percentage do you want to save?: ")),int(input("how much do you get paid an hour?:")),int(input("how many hours do you work a week?: ")))



    attempt= 1
   


    while True:
        payday= input("ENTER THE DAY YOU GET PAID e.g monday: ").capitalize()
        if (attempt % 2) == 0:
            attempt+= 1
            print("These are the available days -", paycheck())
            continue
        elif payday not in paycheck():
            attempt+= 1
            print ("Input is incorrect, Check your spelling")
            continue

        else:

            message= f" Hey {create_account.full_name} I will remind you to save {Savings.final_savings(start)} every {payday}"

            break



    s = smtplib.SMTP('smtp.gmail.com',587)

    s.starttls()

    s.login("kboadu16@gmail.com", "xoaryqsilwhrsseh")

    s.sendmail('&&&&&&&&&&&',create_account.email, message)


    print("REMINDER SUCCESSFULLY SET! CHECK YOUR EMAIL ")



    



