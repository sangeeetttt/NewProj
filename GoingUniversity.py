'''
7. You live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each of the 10 stops on the way. How long will the bus journey take? Alternatively, you could run to university. You jog the first mile at 7mph; then run the next two at15mph; before jogging the last at 7mph again. Will this be quicker or slower than the bus?

'''
#GOING BY BUS
theSpeedOfBusInMin = 25/60
print(f'the bus travells {theSpeedOfBusInMin} in one minute')
#it stops 2 min at each stop for 10 stops.
timeStop = 10*2
print(f'the bus stops for total of {timeStop} minutes.')
#so it takes
timeFor4Miles = 4/theSpeedOfBusInMin
print(f'it takes {timeFor4Miles } min of time to reach the university with out stopping')
totalTimeBus = timeFor4Miles+timeStop
print(f'the total time for reaching university in bus is {totalTimeBus} ')

#WALKING ON FOOT
sevMilesPerHour = 7/60
fifMilesPerHour = 15/60
print(f'converting 7miles per hour in terms of miles per mins, 7/60= {sevMilesPerHour}')
print(f'and converting 15miles per hour in terms of miles per mins, 15/60= {fifMilesPerHour}')
timefor7miles = 2/sevMilesPerHour
timefor15miles = 2/fifMilesPerHour
Otimefor7miles = timefor7miles/2
print(f'If the boy first travels at 7miles for hour for a mile, joggs at 15 miles per hr for other 2 and then walks at 7 miles per hr again,')
totaltimewalking = timefor15miles + timefor7miles
print(f'total time walking= {totaltimewalking} mins')
difference= totaltimewalking-totalTimeBus
if difference<0:
    print('Bus is slower, Walking is faster')
else:
    print('walking is faster')
