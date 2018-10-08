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

print()
print("Weekly Pay:", format(weeklypay, '7.2f'))
print()
print("Monthly Pay:", format(monthlypay, '7.2f'))
print()
print("Yearly Pay:", format(yearlypay, '7.2f'))


         