print 'hello'
print'let\'s get started'

spy_name=raw_input('What is your name?')
if len(spy_name)>0:
    print 'Welcome' +spy_name + '. Glad to have you back with us!'
    spy_salutation=raw_input('What do you want to be referred to as?')
    spy_name=spy_salutation + '' +spy_name
    print 'Alright'  + spy_name + ". i'd like to know more about you before we proceed..."

    spy_age=0
    spy_rating=0.0
    spy_is_online=False

    spy_age=raw_input('what is your age?')
    spy_age = int(spy_age)

if spy_age > 12 and spy_age < 50:
    print("your are of valid age")
else:
    print'you are not of the correct age to spy'


spy_rating=raw_input('what is your spy rating?')
if spy_rating > 4.5:
    print'great ace!'
elif spy_rating > 3.5 and spy_rating <= 4.5:
    print'you are one of the good ones'
elif spy_rating >= 2.5 and spy_rating <= 3.5:
    print'you can always do better'
else:
    print'we can always use somebody to help in the office'

spy_is_online=True
print'Authentication complete.welcome' +\
        spy_name +'age:' +str(spy_age) +\
        'and rating of:' +str(spy_rating) +\
        'proud to have you onboard'










