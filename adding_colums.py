import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('players_20.csv')

data['height_m'] = data['height_cm']/100
data['BMI'] = data['weight_kg']/(data['height_m']**2)

data_out = data[['short_name','overall','height_m','weight_kg','BMI']]
print(data_out)

plt.plot(data['BMI'],data['overall'])
plt.xlabel("Player's BMI")
plt.ylabel("Player's overall performance")
plt.show()