print'Input'
number=raw_input('enter a number')
number=int(number)
if((number)% 3==0) and ((number) % 5==0):
    print'fizzbuzz'
elif((number) % 3==0):
    print'fizz'
elif((number) % 5==0):
    print'buzz'
else:
    print 'number' , number
