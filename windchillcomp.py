from mysci.readdata import read_data
from mysci.printing import print_comparison
from mysci.compuation import compute_windchill

#column names and column indices to read
columns = {'date':0, 'time':1, 'tempout':2, 'windspeed':7, 'windchill':12}

#data types for each column (only if non-string)
types = {'tempout': float, 'windspeed':float, 'windchill':float}

#initialize my data variable

data = {}
for column in columns:
    data[column] = [] 

#read the data file
data = read_data(columns, types=types)

#compute the wind chill temperature
windchill = []
for temp, windspeed in zip(data['tempout'], data['windspeed']):
    windchill.append(compute_windchill(temp, windspeed))

#Output comparison
print_comparison('WINDCHILL', data['date'], data['time'], data['windspeed'],
