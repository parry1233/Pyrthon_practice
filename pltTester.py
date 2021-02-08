import matplotlib.pyplot as plt
import numpy as np

dataX = [0,0,2,3,4]
dataY = [0,1,3,8,9]

print("The last data of X and Y is: ",dataX[-1],",",dataY[-1]) #-1 means the last variable in arrays
plt.plot(dataX,dataY)
plt.show()
plt.clf #clean up and refresh the plot

plt.scatter(dataX,dataY)
plt.show()
plt.clf

data=[20,100,80,90,50,46,60,12,25,69,77,85,88,89,100]
plt.hist(data,bins=10,edgecolor='black')
plt.show()
plt.clf
