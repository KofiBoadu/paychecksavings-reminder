
import datetime 
import calendar
import smtplib


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
            return self.payPeriod


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
              return self.currentMessage()
            return self.otherMessage()


      def currentMessage(self):
            message= f" Hey {self.fullName} save {self.weekSavings()} today"
            s = smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()
            s.login("kboadu16@gmail.com", "xoaryqsilwhrsseh")
            s.sendmail('&&&&&&&&&&&',self.email, message)
            print(f"REMINDER SUCCESSFULLY SET ,YOU GOT PAID TODAY! ,Will remind you to start saving next week {self.payCheckDay}")
          

      def otherMessage(self):
            message= f" Hey {self.fullName} save {self.weekSavings()} on {self.payCheckDay}"
            s = smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()
            s.login("kboadu16@gmail.com", "xoaryqsilwhrsseh")
            s.sendmail('&&&&&&&&&&&',self.email, message)
            print("REMINDER SUCCESSFULLY SET ,CHECK EMAIL")
            



          
   

     

if __name__== '__main__':
      
      userIncome= UserIncomeCalculator(20,25)
      email= EmailReminders("sunday","daniel","mrboadu3@gmail.com",userIncome.percentageToSave,userIncome.hourWage)
      email.set_payPeriod("weekly")
      while True:
        email.checkTodayDate()
        break




