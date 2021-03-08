array1 = ["C.Ronaldo","L.Messi","R.Lewandowski"]
array2 = ["Italy","Spain","Germany"]
array3 = ["Serie A","La Liga","Bundesliga"]

list_data = list(zip(array1,array2,array3))
print('list of zip:')
print(list_data)
print()

#zip data [('C.Ronaldo', 'Italy', 'Serie A'), ('L.Messi', 'Spain', 'La Liga'), ('R.Lewandowski', 'Germany', 'Bundesliga')]
zip_data=zip(array1,array2,array3)

print('each row value of zipped data:')
for value1,value2,value3 in zip_data:
    print(value1," ",value2," ",value3)
print()

#unzip data
print('unzipped data:')
print(*zip(array1,array2,array3))
print()

#asign unzipped data
z = zip(array1,array2,array3)
unzip1,unzip2,unzip3 = z
#unzip1 will be the set of each array's first element  ('C.Ronaldo', 'Italy', 'Serie A')
print('row 1 of zipped data:')
print(unzip1)
print() 


z1 = zip(array1,array2,array3)
#unzipped the data before zipped it again will cahnge the order  [('C.Ronaldo', 'L.Messi', 'R.Lewandowski'), ('Italy', 'Spain', 'Germany'), ('Serie A', 'La Liga', 'Bundesliga')]
zip_reOrder = zip(*z1)
print('unzipped before zipped it again:')
print(list(zip_reOrder))
print()

z1 = zip(array1,array2,array3)
unzip1,unzip2,unzip3 = zip(*z1)
print('row 1 of reordered zipped data:')
print(unzip1) #ReOrdered data will have an different index  ('C.Ronaldo', 'L.Messi', 'R.Lewandowski')
print()