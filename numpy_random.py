import numpy as np

#! seed () 是用來隨機產生整數的亂數
#! 設seed(522)那麼每次生成的結果都會是一樣的整數
np.random.seed(123)

#? 當不指定rand()裡的變數時，會預設生成0~1之間一亂數
print(np.random.rand())
#?再次使用同樣的seed變數，能夠生成一樣之亂數
np.random.seed(123)
print(np.random.rand())


#TODO: create a dice function
def dice(step_in):

    #? roll the dice
    #! rand(a,b) will randomly return a number from a to b, while b is excluded.
    #! ex: randint(1,7) will generate a number from 1 to 6.
    dice=np.random.randint(1,7)
    print('擲到點數: ',dice)

    #* determine the result
    if dice<=2:
        #* 當骰子擲到1,2時，後退一步
        step_in -= 1
    elif dice>2 and dice<=5:
        #* 當骰子擲到3~5時，前進一步
        step_in += 1
    else:
        #* 當骰子擲到6時，重擲一次骰子決定前進步數
        step_in += np.random.randint(1,7)
    
    return step_in


#TODO: 擲骰子遊戲
#* default step will be 50
step = 50
#! 對於不需要用到變數的for迴圈，我們可以設置 " _ " 來跳過命名變數的麻煩!
for _ in range(5):
    step = dice(step)
    print(step)