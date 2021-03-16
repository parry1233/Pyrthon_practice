def args_out(*args):
    s=''
    for value in args:
        s+=str(value)
        print(value)
    
    return 'summary: '+s

def kargs_out(**kargs):
    ss=''
    for key,value in kargs.items():
        ss+=f'key={key}/value={value}'
        print(key,',',value)

    return 'summary: '+ss

print(args_out('one_word'))
print(args_out('one','two','three','four','five'))

print(kargs_out(one='one',two='two',three='three'))
print(kargs_out(one=1,two=2,three=3))
