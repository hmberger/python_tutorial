from mysci.readdata import read_data
from mysci.printing import print_comparison
from mysci.computation import compute_dewpoint

#column names and column indices to read
columns = {'date':0, 'time':1, 'tempout':2, 'humout' : 5, 'dewpt' : 6}

#data types for each column (only if non-string)
types = {'tempout': float, 'humout':float, 'dewpt':float}

#read the data file
data = read_data(columns, types=types)

#compute the dew point temperature
dewpointtemp = [compute_dewpoint(t, h) for t, h in zip(data['tempout'], data['humout'])]

#Output comparison
print_comparison('DEW PT', data['date'], data['time'], data['dewpt'], dewpointtemp)
