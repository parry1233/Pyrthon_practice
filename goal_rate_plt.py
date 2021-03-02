import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('cr7_goal_rate_stat.csv')

print(data['Sporting CP'])

year = np.array([1,2,3,4,5,6,7,8,9])
plt.plot(year,data['Sporting CP'])
plt.plot(year,data['Man United'])
plt.plot(year,data['Real Madrid'])
plt.plot(year,data['Juventus'])
plt.xlabel("year")
plt.ylabel("Goal Rate")
plt.legend(['Sporting CP', 'Man United', 'Real Madrid', 'Juventus'], loc='upper left')
plt.show()