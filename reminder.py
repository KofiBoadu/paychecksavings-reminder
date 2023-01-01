import datetime 
import smtplib
from email.message import EmailMessage
from email.utils import formataddr


class UserIncomeCalculator:
      
      
      def __init__(self,percentageToSave=25,hourWage=20,weekWorkHours=40):
        self.hourWage=float(hourWage)
        self.weekWorkHours=weekWorkHours
        self.percentageToSave=float(percentageToSave)

      def weekGrossIncome(self):
        amount=self.hourWage * self.weekWorkHours
        return amount

      def monthGrossIncome(self):
        return self.weekGrossIncome() * 4

      def annualGrossIncome(self):
        return self.monthGrossIncome()*12
        
      def weekSavings(self):
        amount= self.percentageToSave/100 * self.weekGrossIncome()
        return amount

      def monthSavings(self):
        amount= self.weekSavings() * 4
        return amount

      def annualSavings(self):
        amount= self.monthSavings() * 12 
        return amount
        
         
    
        

class EmailReminders(UserIncomeCalculator):
      
      def __init__(self,payCheckDay="monday",fullName="kaime",email="mrboadu3@gmail.com",percentageToSave=25,hourWage=20,weekWorkHours=40):
        super().__init__(percentageToSave,hourWage,weekWorkHours)
        self.fullName= fullName
        self.email= email
        self.payCheckDay= payCheckDay.capitalize()
        self.payPeriod=0
        self.days= {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
        


      def set_payPeriod(self,payPeriod):
            if payPeriod=="weekly":
              self.payPeriod= 7
           
            if payPeriod=="biweekly":
              self.payPeriod=14

      def get_payPeriod(self):
            if self.payPeriod== 7:  
              return "week"
            return "two-weeks"
           


#there is a bug in this function cant handle two weeks dates well and needs to be fixed 

      def next_PayDate(self):
            weekday= 0
            for key, value in self.days.items():
              if self.payCheckDay in value:
                weekday= key
            day= datetime.datetime.now().date()
            date= day+ datetime.timedelta((weekday-day.weekday()) % self.payPeriod)
            return date
            
            
        #there is a bug in this function it can only calculate the next week and two weeks if the day is in the past cant to future days right now 

      def checkTodayDate(self):
            day= datetime.datetime.now().date().weekday()
            dayName= self.days[day]
            if self.payCheckDay== dayName:
              return self.firstMessage()
            return self.secondMessage()


      def firstMessage(self):
            senderEmail= "kboadu16@gmail.com"
            msg = EmailMessage()
            msg["Subject"] = "Paycheck Savings Reminder"
            msg["From"] = formataddr(("KAIME.CORP", f"{senderEmail}"))
            msg["To"] = self.email
            msg["BCC"] = senderEmail
            msg.set_content(
                              f"""\
                              Hi {self.fullName},
                              Thank you for signing up with KAIME Savings!
                              You got paid Today and I will start reminding you to save <strong style="color:green;">USD{self.weekSavings()}</strong> every {self.payCheckDay}.

                              
                              """
                          )
            msg.add_alternative(
              f"""\
          <html>
            <body>
              <p>Hi {self.fullName},</p>
              <p>Thank you for signing up with KAIME Savings!</p>
              <p>You got paid Today and I will  start reminding you to save <strong style="color:green;">USD{self.weekSavings()}</strong> every {self.payCheckDay}.</p>
              <p>Best Regards </p>
              <strong style="color: red ;">KAIME</strong>
            </body>
          </html>
          """,
              subtype="html",
          )

            s = smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()
            s.login("kboadu16@gmail.com", "xoaryqsilwhrsseh")
            s.sendmail(senderEmail,self.email,  msg.as_string())
            return f"REMINDER SUCCESSFULLY SET ,YOU GOT PAID TODAY! ,Will remind you to start saving every {self.get_payPeriod()} on {self.payCheckDay}"
          

      def secondMessage(self):
            senderEmail= "kboadu16@gmail.com"
            msg = EmailMessage()
            msg["Subject"] = "Paycheck Savings Reminder"
            msg["From"] = formataddr(("KAIME.CORP", f"{senderEmail}"))
            msg["To"] = self.email
            msg["BCC"] = senderEmail
            msg.set_content(
                              f"""\
                              Hi {self.fullName},
                              Thank you for signing up with KAIME Savings!
                              I will remind you every {self.get_payPeriod()} to save USD{self.weekSavings()} from your PAYCHECK. 
                              Your next saving date should be {self.next_PayDate()} and I will send you a reminder !
                              KAIME 
                              """
                          )
            msg.add_alternative(
              f"""\
          <html>
            <body>
              <p>Hi {self.fullName},</p>
              <p>Thank you for signing up with KAIME Savings!</p>
              <p>I will remind you every <strong style="color:red;">{self.get_payPeriod()}</strong> to save <strong style="color:green;">USD{self.weekSavings()}</strong> from your PAYCHECK. </p>
              <p>Best regards</p>
              <strong style="color:red;">KAIME</strong>
            </body>
          </html>
          """,
              subtype="html",
          )

            s = smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()
            s.login("kboadu16@gmail.com", "xoaryqsilwhrsseh")
            s.sendmail(senderEmail,self.email,  msg.as_string())
            return f"REMINDER SUCCESSFULLY SET ,Will remind you to start saving every {self.get_payPeriod()} on {self.payCheckDay} CHECK EMAIL for verification \n next pay date is {self.next_PayDate()}" 
    
            

     
    
            





          
   

     

