def calling(word1, echo=1):
    '''
    Concatenate echo copies of word1 and three exclamation marks at the end of the string
    '''

    if echo<0:
        raise ValueError('echo cannot be an integer that less than 1')

    try:
        echo_word = word1 * echo + '!!!'
        return echo_word
    except:
        print('other excpection is handled.')

#print(calling([1,2,3],echo=3)) #raise value error
#print(calling('Try',echo=-2)) #other exception
print(calling('Try',echo=3))