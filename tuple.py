data = ["first","second","third","forth","fifth"]

#create tuple
tuple_data1 = enumerate(data)
list_data = list(enumerate(data))
print(list_data)
for index,value in tuple_data1:
    print(index," ",value)

#create tuple from index 1
tuple_data2 = enumerate(data,start=1)
for index,value in tuple_data2:
    print(index," ",value)