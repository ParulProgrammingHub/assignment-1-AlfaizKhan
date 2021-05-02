rate = int(input('Enter rate percentage'))
principle = float(input('Enter the principle amount'))
x = int(input('Select 1 for duration of time in days  \n2 for time in months and \n3 for time in years'))

if(x == 1):
	time = int(input('Enter number of days'))
	time = time /(12*30)
elif(x == 2):
        time = int(input('Enter number of months'))
        time = time / 12
else:
        time = int(input(' Enter number of years'))
	
def Simple_Interest(rate,principle,time):
    simple_Interest = ( principle * rate * time ) / 100
    print(f'Simple Interest = {simple_Interest}')

    total = principle + simple_Interest
    print(f'Total amount = {total}')
Simple_Interest(rate,principle,time)

