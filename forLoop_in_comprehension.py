
#TODO: print the first character in each string
name = ['Perry','Chung','AMDyes','RTX3070']
all_first_character = [character[0] for character in name]
print(all_first_character)

#TODO: print each of the square root from 0 to 9
square_root = [a**2 for a in range(0,10)]
print(square_root)

#TODO: create and print a 5*5 matrix
'''
example:
matrix = [[0,1,2,3,4],
          [0,1,2,3,4],
          [0,1,2,3,4],
          [0,1,2,3,4],
          [0,1,2,3,4]]]
'''

matrix = [[column for column in range(0,5)] for row in range(0,5)]
print(matrix)
for each_column in matrix:
    print(each_column)

#TODO: sorting function
new_name = [n for n in name if len(n)<=5]
print(new_name)

#TODO: if-else function
#? if len(n)<=5 do nothing, else replace the string
new_name2 = [n if len(n)<=5 else 'over 5 characters' for n in name]
print(new_name2)

#TODO: dictionary
name_dict = {name.index(member) : member for member in name}
print(name_dict)