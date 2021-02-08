myArray = ["first","second","third","forth","fifth"]

print("iterate call by for loop (current type--",myArray,"):")
for array in myArray:
    print(array)

myIterate=iter(myArray)

print("iterate call by iterate (current type--",myIterate,"):")
print(myIterate)
print(next(myIterate))
print(next(myIterate))
print(next(myIterate))
print(next(myIterate))
print(next(myIterate))
