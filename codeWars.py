def is_isogram(string):
    # your code here
    word = string.lower()
    isogram = ""
    for n in word:
        if n not in isogram:
            isogram += n
    print (isogram)
    if word == isogram:
        return True
    else:
        return False




is_isogram = is_isogram("apple")
print(is_isogram)

def add_binary(a,b):
    return '{0:b}'.format(a + b)

z=add_binary(2,0)
print(z)

