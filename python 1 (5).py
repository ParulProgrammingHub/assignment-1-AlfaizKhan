days=int(input('enter no. of days'))
year=days/360
a=days%360
b=a//30
c=a%30
print 'no. of year=',year
print 'no. of months	=',b
print 'no. of days=',c
