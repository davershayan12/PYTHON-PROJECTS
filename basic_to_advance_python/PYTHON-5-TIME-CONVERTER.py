#there are two method to convert time in seconds to days, hours, minutes and seconds.
#Method 1(main):
time=int(input('enter your time in seconds:'))
days=time//86400
hours=(time%86400)//3600
minutes=(time%3600)//60
seconds=time%60
print(f"days: {days},hours: {hours},minutes: {minutes},seconds: {seconds}")
