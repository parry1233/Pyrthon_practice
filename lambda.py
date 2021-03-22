'''
simple anonymous function
'''
raise_to_power = lambda x,y: x**y
print(raise_to_power(2,3))  #*2^3 = 8

echo_word = (lambda word,times: word*times)
result = echo_word('Hi',5)
print(echo_word)

'''
map() applies the function to ALL elements in the sequence
map() function contains two arguments: map(func,seq)
'''
nums_list=[48,6,9,21,1]
square_all = map(lambda num: num **2, nums_list)
print(square_all) #* will print out a map object
print(list(square_all)) #* [48^2, 6^2, 9^2, 21^2, 1^2]

spells = ['one','two','three','four','five']
spells_map = map(lambda each_spell: each_spell * 3, spells)
print(type(spells_map))
print(list(spells))

'''
filter() function should check all the element in the sequence
'''
player_list = [
    ['lewy',91],
    ['ronaldo',92],
    ['messi',93]
]
#* [[player name, rating], [player name, rating], ... ]

result = filter(lambda check: check[1]>=92, player_list) #? check if rating is over or equal to 92
print(list(result))

'''
import REDUCE function from  functools
reduce() function can concatenate all elements to a string
'''
from functools import reduce
stark = ['one','two','three','four','five']
result = reduce(lambda item1,item2: item1+item2, stark)
print(result)

