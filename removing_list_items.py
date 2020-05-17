def array_diff(a, b):
    #your code here
    if len(a) > len(b):
        for j in range(int(len(a))):
            for i in b:
                if i in a:
                    a.remove(i)
    else:
        for j in range(int(len(b))):
            for i in a:
                if b[j] in a:
                    a.remove(b[j])

    return(a)
    

a = [12, -11, 11, -14, -13, 10]
b = [4, -16, 10, -19, 8, -11, -14, 6, 12]
print(array_diff(a,b))

