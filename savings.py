from datetime import datetime
import calendar
import smtplib

#imported these modules to perfom the following task
# the datetime module will determine or tell  the program the current day of the week e.g mon,tues
# the calendar module has a method that returns all the days of the week in intergers which will be needed 
#the smtplib will be resourceful to send out our emails.

class Signup:
    
    def __init__(self,full_name,email):
        
        self.full_name=full_name
        self.email=email
        
    def __str__(self):
        
        return f"hey {self.full_name} welcome"

#my sign up class creates just a simple profile 
        
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
    
    # This savings class has methods that returns an employee work benefits and wages . 
    #you can check your weekly ,monthly and annual income by instatantianting any of the functions or methods

    
def paycheck():
    
    days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    
    return days

# Over here i created a simple function to store and return all the days of the week in strings . 
# I used this approach due to the fact that, I couldnt find any function or module that return days of the week
# as a string .


if __name__== '__main__':

    # called __main__ as an entry point to  run the program 
    
    create_account= Signup(input("full name: "),input("email: "))
    print(f"Hey {create_account.full_name} fill out the forms below and start SAVING!")
    start= Savings(int(input("what percentage do you want to save?: ")),int(input("how much do you get paid an hour?:")),int(input("how many hours do you work a week?: ")))

   # Using the input function to collect data from user to meet the conditions below in our WHILE-TRUE

    attempt= 1
   
    #To avoid user from making many wrong attempts I decided to limit attempts to just twice 

    while True:

    # To keep the program running until a condition is met ,using while loop was my best option 
        
        
        
        weekdays1= []

        days= ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    
    # I declared the days of the week to be able to meet to compare it to the interger days of the week 
    # from the calendar module.

        a=calendar.Calendar(firstweekday=0)

    #The default value for the caelendar.firstweekday is 0 which is Monday

        [weekdays1.append(i) for i in a.iterweekdays()]

    # I iterated and appened the integer values of the weekdays in a list which i later intended to use.
        
        x= dict(zip(weekdays1,days))

    # I wanted my program to recognize the string days same as it does for the calendar weekday method.

    # i zipped two list into a dictionary with the interger weekdays as keys and my declared string week days as values

        payday= input("enter day: ").capitalize()
        
    # to avoid any exceptions i decided to capitalize every first letter of the input fromm the user 
     
        for key,value in x.items():
            
            if payday in value:
                
                
                a.firstweekday=key

     # One issue i noticed is, the weekday in calendar always start from monday and i wanted to change
     # to start from the day the user specifies as her payday. for example if i want the program to send 
     # reminder every tuesday i will need to know the starting day of the week . so whenever a user 
     # specifies her check comes in tuesdays the program sets the first day of the week to that day .    
            
        today= datetime.now() 

        current=calendar.weekday(today.year, today.month, today.day)

        #from the datetime module ,datetime.now tells you the current day and to be sure it 
        #updates every day i used the calendar.weekday on the methods in the datetime.now

        
        if (attempt % 2) == 0:
            attempt+= 1
            print("These are the available days -", paycheck())
            continue
            
        elif payday not in paycheck():
            attempt+= 1
            print ("Input is incorrect, Check your spelling")
            continue

        #setting attempts overhere and to check if all char are spelt correctly
        
        else:
            
            
            
            if a.firstweekday == current:
                
            #I specified here that , if the firsday of the week which authomatically sets to
            #the user paycheck day , the program should compare it to see if its the same day as of today,
            #if the both days a the same the email sends.
                
                message= f" Hey {create_account.full_name} save {Savings.final_savings(start)} today"
    
                s = smtplib.SMTP('smtp.gmail.com',587)

                s.starttls()

                s.login("kboadu16@gmail.com", "xoaryqsilwhrsseh")

                s.sendmail('&&&&&&&&&&&',create_account.email, message)
                
                print(f"REMINDER SUCCESSFULLY SET ,YOU GOT PAID TODAY! ,Will remind you to start saving next week {payday}")

    
                break
        
            
            else:
                
          #if the paycheck day isnt the same as the day of signing up the program starts reminders the following
          #weekday..

                message= f" Hey {create_account.full_name} I will remind you to save {Savings.final_savings(start)} every {payday}"

                s = smtplib.SMTP('smtp.gmail.com',587)

                s.starttls()

                s.login("kboadu16@gmail.com", "xoaryqsilwhrsseh")

                s.sendmail('&&&&&&&&&&&',create_account.email, message)

                print("REMINDER SUCCESSFULLY SET! CHECK EMAIL")



  



            
            

       
            
                

    
    
    
    
 


