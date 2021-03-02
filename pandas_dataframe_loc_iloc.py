import pandas as pd
data = pd.read_csv('players_20.csv',index_col=2)

print(data['overall']) #print as pandas series
print(data[['overall']]) #print as pandas dataframe


"""loc and iloc"""

#primt out specific row as pandas series
print(data.loc['L. Messi'])
print(data.iloc[0])
#this two are have same result

#print out specific rows as pandas dataframe
print(data.loc[['L. Messi','Cristiano Ronaldo']])
print(data.iloc[[0,1]])
#this two are have same result

#print out specific rows and columns (rows goes first while columns are specified after comma)
print(data.loc[['L. Messi','Cristiano Ronaldo'],['overall','potential']])

print(data.loc[:,['overall','potential']])
print(data.iloc[:,[9,10]])
#above two lines have the same result
