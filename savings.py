from datetime import datetime
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
    self.days= {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
   
  
  def setFirstDay(self):
    date= calendar.Calendar(firstweekday=self.setNewWeekDay())
    for i in date.iterweekdays():
      print(i)
       

  def setNewWeekDay(self):
    for key,value  in self.days.items():
      if self.payCheckDay in value:
        startDay=key
    return startDay


  def checkTodayDate(self):
    today= datetime.now()
    currentDate= calendar.weekday(today.year, today.month, today.day)
    if self.setNewWeekDay()== currentDate:
      sendMessage= self.currentMessage()
      return sendMessage
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
  email= EmailReminders("tuesday","daniel","mrboadu3@gmail.com",userIncome.percentageToSave,userIncome.hourWage)
  while True:
    email.checkTodayDate()
    break


  



