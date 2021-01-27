from mysci.readdata import read_data
from mysci.printing import print_comparison
from mysci.computation import compute_heatindex

#column names and column indices to read
columns = {'date':0, 'time':1, 'tempout':2, 'humout' : 5, 'heatindex' : 13}

#data types for each column (only if non-string)
types = {'tempout': float, 'humout':float, 'heatindex':float}

#initialize my data variable

data = {}
for column in columns:
    data[column] = [] 

#read the data file
data = read_data(columns, types=types)

#compute the heat index
heatindex = []
for temp, humout in zip(data['tempout'], data['humout']):
    heatindex.append(compute_heatindex(temp, humout))

#Output comparison
print_comparison('HEAT INDEX', data['date'], data['time'], data['heatindex'], heatindex)
