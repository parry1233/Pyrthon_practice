import numpy as np
file = "推甄時程整理.csv"

#basic load TXT function
#original = np.loadtxt(file,delimiter=',',skiprows=1,encoding='utf-8',dtype=str)
#print(original)

#generate from TXT function
gen = np.genfromtxt(file,delimiter=',',names=True,dtype=None)
print(gen)
#print(*gen)
row1,row2,row3,row4,row5,row6,row7,row8,row9,row10,row11,row12 = gen
print(row1)

"""
#receive from CSV function
#recfromcsv method only need to pass file name because it has defaults delimiter=',' and names=True in addition to dType=None 
rec = np.recfromcsv(file)
print(rec[:3]) #[:3] means get the rows from index 0 to index 2 (3 rows counted), furthermore, [2:4] means start at index 2 and and end at index 4 (index 4 is not imcluded)
"""