import random
import time
def getrandomdate(startDate,endDate):
    print("IDK wht i making",startDate, " and " , endDate )
    randomgenerator = random.random()
    dateformat = '%m/%d/%Y'
    starttime = time.mktime(time.strptime(startDate,dateformat))
    endtime = time.mktime(time.strptime(endDate , dateformat))
    
    randomtime = starttime + randomgenerator * (endtime - starttime)
    randomdate = time.strftime(dateformat, time.localtime(randomtime))
    return randomdate
    
print("Random Date = ",getrandomdate("1/1/2025" , "12/12/2025"))
