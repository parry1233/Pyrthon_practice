import pandas as pd
data = pd.read_csv('player_data1.csv',index_col=0)
print(data)

#TODO: iterate over rows
'''
for row in data.iterrows():
    print(row)
'''

#? try iterate over row and index
'''
for rowLabel ,rowData in data.iterrows():
    print(rowLabel)
    print(rowData)
'''

#TODO: add column of uppercase league
'''
#? method 1
for index,row in data.iterrows():
    #! creating series on every iteration
    data.loc[index, 'Upper'] = row['league'].upper()
print(data)
'''
'''
#? method 2
data['Upper'] = data['league'].apply(str.upper)
print(data)
'''

#TODO: