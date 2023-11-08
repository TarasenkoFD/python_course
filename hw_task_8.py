def abbreviature(string):
    if not type(string) is str:
        raise Exception('Wrong format')
    Abb = string[0]
    for i in range(1,len(string)-1):
        if string[i] == ' ':
            Abb += string[i+1]

    return(Abb)

A = 'Test strok na abbreviaturu'
print(abbreviature(A))

