import datetime 
import smtplib
from email.message import EmailMessage
from email.utils import formataddr


class UserIncomeCalculator:
      
      
      def __init__(self,percentageToSave,hourWage,weekWorkHours=40):
        self.hourWage=hourWage
        self.weekWorkHours=weekWorkHours
        self.percentageToSave=percentageToSave

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
      
      def __init__(self,payCheckDay,fullName,email,percentageToSave,hourWage,weekWorkHours=40):
        super().__init__(percentageToSave,hourWage,weekWorkHours)
        self.fullName= fullName
        self.email= email
        self.payCheckDay= payCheckDay.capitalize()
        self.payPeriod=0
        self.days= {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
        


      def set_payPeriod(self,payPeriod):
            if payPeriod=="weekly":
              self.payPeriod= 7
            else:
              self.payPeriod=14

      def get_payPeriod(self):
            if self.payPeriod== 7:  
              return "week"
            return "two-weeks"
           


      def next_PayDate(self):
            weekday= 0
            for key, value in self.days.items():
              if self.payCheckDay in value:
                weekday= key
            day= datetime.datetime.now().date()
            date= day+ datetime.timedelta((weekday-day.weekday()) % self.payPeriod)
            return date
                
        

      def checkTodayDate(self):
            currentDate= datetime.datetime.now().date()
            if self.get_payPeriod()== currentDate:
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
                              I hope you are well.
                              I just wanted to drop you a quick note to remind you to save {self.weekSavings()} USD today.
                              KAIME LLC
                              """
                          )
            msg.add_alternative(
              f"""\
          <html>
            <body>
              <p>Hi {self.fullName},</p>
              <p>I hope you are well.</p>
              <p>I just wanted to drop you a quick note to remind you to save <strong style="color:green;">{self.weekSavings()}USD</strong> today.</p>
              <p>Best regards</p>
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
            print(f"REMINDER SUCCESSFULLY SET ,YOU GOT PAID TODAY! ,Will remind you to start saving every {self.get_payPeriod()} on {self.payCheckDay}")
          

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
                              I hope you are well.
                              I just wanted to drop you a quick note to remind you save {self.weekSavings()} USD .
                              KAIME 
                              """
                          )
            msg.add_alternative(
              f"""\
          <html>
            <body>
              <p>Hi {self.fullName},</p>
              <p>I hope you are well.</p>
              <p>I just wanted to drop you a quick note to remind you to save  <strong style="color:green;">{self.weekSavings()}USD</strong></p>
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
            print(f"REMINDER SUCCESSFULLY SET ,Will remind you to start saving every {self.get_payPeriod()} on {self.payCheckDay} CHECK EMAIL for verification \n next pay date is {self.next_PayDate()}" )
    
            
         



if __name__== '__main__':
      
      userIncome= UserIncomeCalculator(20,25)
      email= EmailReminders("tuesday","daniel","mrboadu3@gmail.com",userIncome.percentageToSave,userIncome.hourWage)
      email.set_payPeriod("biweekly")
      while True:
        email.checkTodayDate()
        print(email.next_PayDate())
        break


