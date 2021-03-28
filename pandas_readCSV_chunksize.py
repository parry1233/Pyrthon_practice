import pandas as pd
import matplotlib.pyplot as plt

#? read 100 data at one time
chunk_reader = pd.read_csv('players_20.csv',chunksize=100)

#? initialize an empty dataframe
data = pd.DataFrame()

#TODO: iterate over each chunk
for players_data in chunk_reader:
    overall_and_age = zip(players_data['overall'],players_data['age'])

    #? Turn zip object into list
    overall_and_age = list(overall_and_age)
 
    data = data.append(overall_and_age)

print(data)
data.plot(kind='scatter',x=1,y=0)
plt.xlabel('age')
plt.ylabel('overall')
plt.show()