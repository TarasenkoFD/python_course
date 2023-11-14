def common(list_1, list_2):
    return list(filter(lambda x: x in list_2, list_1))


A = [1, 2, 3, 'test', 'pipa', True, [1,2,3], (1,2,4)]
B = [0, 2, 3, 'terst', 'pipa', True, [0,2,3], (1,2,4)]

print(common(A,B))