
import datetime 
import random 
currentDate = datetime.date.today()


range_start = 10**(5-1)
range_end = (10**5)-1
randomNumber = random.randint(range_start, range_end)
    
gasCode =  currentDate.strftime("%j")+'800'+str(randomNumber)

print(gasCode)
