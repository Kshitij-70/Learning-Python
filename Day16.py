from datetime import datetime
now=datetime.now() 
 
#Get the current day, month, year, hour, minute and timestamp from datetime module
day=now.day
month=now.month
year=now.year
hour=now.hour
minute=now.minute
timestamp=now.timestamp()
print(day, month, year, hour, minute, timestamp )

#Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
date=now.strftime("%m/%d/%Y, %H:%M:%S")
print(date)

