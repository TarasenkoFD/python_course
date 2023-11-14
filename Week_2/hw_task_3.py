def type_check(*args):
    return tuple(filter(lambda x: isinstance(x, str), args))


A = [1,2,3]
B = 'tesr'
C = True
D = False
E = 1.0
F = 'doubl1e'

print(type_check(A,B,C,D,E,F))