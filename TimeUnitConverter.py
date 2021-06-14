'''
10. Write a Python program to convert seconds to day, hour, minutes and seconds.
'''
seconds= int(input('Enter the time in seconds: '))
inMin = seconds/60
inHour = seconds/(60*60)
inDay = seconds/(60*60*24)
print(f'in Minutes= {inMin}')

print(f'in Hours= {inHour}')

print(f'in Days= {inDay}')

