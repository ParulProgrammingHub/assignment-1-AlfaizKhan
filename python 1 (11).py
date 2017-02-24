amount = input('Enter the principal amount')
amount = float(amount)
rate = input('Enter rate percentage')
x = input('Press \'1\' for duration of time in days  \n\'2\' for time in months and \n\'3\' for time in years\n')
if(x == 1):
        time = input('Enter number of days')
        time = time /(12*30)
elif(x == 2):        
        time = input('Enter number of months')
        time = time / 12
else:
        time = input(' Enter number of years')
def Compound_Interest(amount,rate,time):
    total_amount = (amount * (1 + (float(rate)/100))**time)
    print('\nTotal Amount is %f' %total_amount)

    compound_interest = total_amount - amount
    print('\nCompound Interest = %f' %compound_interest)
    print('\nTotal amount = %f' %total_amount)
s=Compound_Interest(amount,rate,time)
