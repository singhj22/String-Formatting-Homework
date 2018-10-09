'''
Created on Oct 5, 2018
@author: Jugat Singh
Python Pd.5 Even
'''

rate= float(input('Please enter your hourly rate: '))

hours= float(input('Please enter the hours worked per day: '))

weeklypay = rate *hours*7
monthlypay = rate *hours*31
yearlypay = rate *hours*365

print("\n\n\nSalaries:")
print("\t"+ format("Weekly Pay:",'<20s>') + format(weeklypay,'>10,.2f'))
print("\t"+ format("Monthly Pay:",'<20s>') + format(monthlypay,'>10,.2f'))
print("\t"+ format("Annual Pay:",'<20s>') + format(yearlypay,'>10,.2f'))
