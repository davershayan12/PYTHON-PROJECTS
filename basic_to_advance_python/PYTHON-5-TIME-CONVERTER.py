#there are two method to convert time in seconds to days, hours, minutes and seconds.
#Method 1:
time=int(input('enter your time: '))#take time in seconds
days=int(time/86400)# Calculate the number of days by dividing the time by the total seconds in a day (86400)
hours=int((time%86400)/3600)# Calculate the number of hours by finding the remainder of time after days and dividing by the total seconds in an hour (3600)
minutes=int((time%3600)/60)# Calculate the number of minutes by finding the remainder of time after extracting hours and dividing by 60
seconds=time%60# Calculate the remaining seconds after extracting days, hours, and minutes
print(f"days: {days},hours: {hours},minutes: {minutes},seconds: {seconds}")#answer


#method 2(main):
time=int(input('enter your time in seconds:'))#take time in seconds
days=time//86400 # Calculate the number of days by dividing the time by the total seconds in a day (86400)
hours=(time%86400)//3600 # Calculate the number of hours by finding the remainder of time after days and dividing by the total seconds in an hour (3600)
minutes=(time%3600)//60 # Calculate the number of minutes by finding the remainder of time after extracting hours and dividing by 60
seconds=time%60 # Calculate the remaining seconds after extracting days, hours, and minutes
print(f"days: {days},hours: {hours},minutes: {minutes},seconds: {seconds}")#answer
