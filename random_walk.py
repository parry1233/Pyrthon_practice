import numpy as np
import matplotlib.pyplot as plt

all_walks = []
for every_round in range(500):
    each_round_walk_log = [0]
    for walk in range(100):
        step = each_round_walk_log[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            #? when dice point is less or equal to 2, then go backward for one step
            #? if current step is less than 0, it will be 0
            step = max(0,step-1)
        elif dice <= 5:
            step += 1
        else:
            step += np.random.randint(1,7)
        
        each_round_walk_log.append(step)
    all_walks.append(each_round_walk_log)

#transform all_walks from list to tuple
all_walks_transform = np.array(all_walks)

#TODO: calculate the percentage of each round that end up with over 30 steps 
over_30stpes_precentage = np.mean(all_walks_transform[:,-1]>30)
print(over_30stpes_precentage)

#TODO: create and plot
#? transpose x and y to fit histogram
all_walk_transpose = np .transpose(all_walks_transform)
#? get each round last step position
ends = all_walk_transpose[-1,:]

plt.hist(ends)
plt.show()


