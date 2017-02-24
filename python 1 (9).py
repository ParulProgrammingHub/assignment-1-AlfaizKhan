print 'Each Exam is of 50 marks'
a=int(input('marks of 1st subject:'))
b=int(input('marks of 2nd subject:'))
c=int(input('marks of 3rd subject:'))
d=int(input('marks of 4th subject:'))
e=int(input('marks of 5th subject:'))
prc=((float(a+b+c+d+e)/250)*100)
print prc
if prc<35.0:
    print 'FAIL'
else:
    print 'PASS'

