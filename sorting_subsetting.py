import pandas as pd
data = pd.read_csv("players_20.csv",index_col=2)
#change data's index to specific column

"""
#sort by value
individual = 'overall'
print(data.sort_values(individual,ascending=False)) # ascending=False allow a descending order

#sort by multiple value
multiple = ['overall','age'] # compare overall value first, while encounter same overall value, then compare age value
allow_ascending = [False,True] # overall value will be a descending order, but age value will be an ascending order
print(data.sort_values(multiple,ascending=allow_ascending))

#show the value you needed
print(data[['short_name','overall']])

"""
#show limited or specify value
print(data[data['overall']>90])
overall_limited = data['overall']>90
age_limited = data['age']==28
print(overall_limited) # print the result (true or false) according to the limit
#print(data[(overall_limited) & (age_limited)]) # be metion that '()' is needed or the code will be an error

"""
#substetting (子集合)
name = ['L. Messi','Cristiano Ronaldo','Neymar Jr']
condition = data['short_name'].isin(name)
print(data[condition])
"""