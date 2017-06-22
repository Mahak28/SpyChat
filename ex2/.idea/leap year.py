print'input:'
year=raw_input('enter a year')
year=int(year)
if(year%4==0):
    print'it is a leap year'
elif(year%400==0):
    print'it is a leap year'
elif(year%100==0):
    print'it is not a leap year'
else:
    print'it is not a leap year'