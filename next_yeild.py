
#TODO: get player's name from large file

def read_large_file_GetName(file_object):

    #! skip the first column (columns' name)
    file_object.readline()

    while True:
        #? read a line from the file
        data = file_object.readline()

        #?break if this is the end of the data
        if not data:
            break
        #? yield the line of the data, get the name from the data of each line
        else:
            '''
            #! yield 設計來的目的，就是為了單次輸出內容
            #! 可以把 yield 暫時看成 return，但是這個 return 的功能只有單次
            #! 一旦我們的程式執行到 yield 後，程式就會把值丟出，並暫時停止。直到下一次的遞迴，程式才會從 yield 的下一行開始執行
            '''
            yield data.split(',')[2]



with open('players_20.csv',encoding='utf-8') as file:
    GetName = read_large_file_GetName(file)
    print(next(GetName))
    print(next(GetName))
    print(next(GetName))





#TODO: count plyers' overall and analyze

def read_large_file_getOverall(file_object):
    
    #! skip the first column (columns' name)
    file_object.readline()

    while True:
        #? read a line from the file
        data = file_object.readline()

        #?break if this is the end of the data
        if not data:
            break
        #? yield the line of the data, get the name from the data of each line
        else:
            '''
            #! yield 設計來的目的，就是為了單次輸出內容
            #! 可以把 yield 暫時看成 return，但是這個 return 的功能只有單次
            #! 一旦我們的程式執行到 yield 後，程式就會把值丟出，並暫時停止。直到下一次的遞迴，程式才會從 yield 的下一行開始執行
            '''
            yield data.split(',')[10]

#? initialize a dictionary
counts_dict ={}

with open('players_20.csv',encoding='utf-8') as file:
    for overall in read_large_file_getOverall(file):
        if overall in counts_dict.keys():
            counts_dict[overall] += 1
        else:
            counts_dict[overall] = 1

print(counts_dict) 
