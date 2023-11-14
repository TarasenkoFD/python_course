def kratnost(spisok):
    print('vvedi chislo')
    value = int(input())
    return list(filter(lambda x: x % value == 0, spisok))

A = [1,2,3,4,5,6,7,8,9,10]
print(kratnost(A))