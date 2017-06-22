#input value
n=15
#empty string
s=""
if n%3==0:
    s+="fizz"
if n%5==0:
        s+="buzz"
if s=="":
         print n
else:
            print s