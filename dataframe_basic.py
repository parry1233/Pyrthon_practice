import pandas as pd
file = "player_data.csv"
data = pd.read_csv(file,encoding='utf-8')

#print 0-4 index of the data
print("head function:")
print(data.head())

#print data information, which will show each of the columns sucj as the type and number of missing code
print("info function:")
print(data.info())

#print out caculations of few summary staistics for each column
print("describe function:")
print(data.describe())

#print the number of rows and colums of the dataframe
print("shape value:")
print(data.shape)

#print the values of dataframe
print("value:")
print(data.values)

#print the colums of dataframe
print("columns value:")
print(data.columns)

#print row index of dataframe
print("index value:")
print(data.index)