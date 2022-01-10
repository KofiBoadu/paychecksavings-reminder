import datetime

import calendar

import smtplib


print("HEY START GETTING REMINDERS AND SAVE MORE !!")

print("""


""")


user = input("FULL NAME: ")
user_email = input("EMAIL ADDRESS: ")


print("""



""")




print("HEY ! GET READY TO START SAVING!")


print("""



""")

mysavings=int(input("WHAT PERCENTAGE DO YOU WANT SAVE ? %: "))

hourwage= int(input("HOW MUCH DO YOU GET PAID EVERY HOUR?: "))

work_hours_week=int(input("HOW MANY HOURS DO YOU WORK PER WEEK: "))

weekly= hourwage*work_hours_week

monthly= weekly*4

annually= monthly*12

savingresults= (mysavings/100)*weekly




payday= input("ENTER THE DAY YOU GET PAID e.g monday: ").capitalize()

week_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

week_num=datetime.datetime.today()



for i in week_days:
    
    if payday==i:
        
        message =(f"AWSEOME!{user}.I WILL REMIND YOU TO SAVE ${savingresults} FROM YOUR PAYCHECK EVERY {payday}!!!")


s = smtplib.SMTP('smtp.gmail.com',587)

s.starttls()

s.login("kboadu16@gmail.com", "xoaryqsilwhrsseh")

s.sendmail('&&&&&&&&&&&',user_email, message)


print("""



""")



print("REMINDER SUCCESSFULLY SET! CHECK YOUR EMAIL ")



        



