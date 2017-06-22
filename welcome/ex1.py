print('Input:')
first_name=raw_input('enter first name')
last_name=raw_input('enter last name')
gender=raw_input('enter your gender')
mobile_number=raw_input('enter your mobile number')
email_id=raw_input('enter your email')
amount=raw_input('enter amount paid')

amount=int(amount)

if(gender=='male'):
    salutation='Mr.'
else:
    salutation='Ms.'
print('Output')
print 'to'+email_id
print 'mobile:'+mobile_number
print 'Hi!' +salutation+first_name+last_name+'!'
if(amount==2499):
    print 'Welcome to Acadview Internship program! We have successfully received the payment of Rs.2499.'
elif(amount<2499):
    amount=2499-amount
    print 'Welcome to Acadview! you have remaining balance:',amount,