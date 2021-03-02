import pandas as pd
names = ['United States','Australia','Japan','India','Russia','Morocco','Egypt']
dr =[True,False,False,False,True,True,True]
cpc=[809,731,588,18,200,70,45]

cars_dict={'country':names,'drives_right':dr,'cars_per_capital':cpc}

print('Before dataframed:')
print(cars_dict)

print('After dataframed:')
cars_df=pd.DataFrame(cars_dict)
print(cars_df)

#specify rows label
row_labels = ['US','AUS','JPN','IN','RU','MOR','EG']
cars_df.index = row_labels
print(cars_df)