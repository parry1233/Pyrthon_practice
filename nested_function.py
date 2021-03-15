
#TODO: Nonlocal variable in a nested function
def print_msg():
    #? this is the outer enclosing function
    n = 'I am outer (nonlocal) variable'

    def printer():
        nonlocal n
        n = 'I am inner (local) variable'
        return n

    print(printer())

print_msg()


#TODO: nested function with closures
def nested():

    def inner_func():
        return 'inner function'

    return inner_func #! there's no '()' here

print(nested())
print(nested()())


#TODO: nested functions with closures that contained input value
def GoGo(gogo_word):

    def inner(team_name):
        combined = team_name + gogo_word*3
        return combined

    return inner #! there's no '()' here

gogo = GoGo('go')
print(gogo)
print(gogo('Uni lions'))
